# -*- coding: iso-8859-15 -*-

from Django.globals import *
from Django.Banking.models import *

import time
from decimal import *
import shlex
from subprocess import Popen, PIPE


def define(source, field):
	field	= ' '+field.replace('", "', '\n')+'="'
	p	= source.find( field )
	if p > -1:
		p += len( field )
	else:
		return ""
	q	= source.find('"', p)
	return source[p:q]


def SWIFTdate( source ):
	day	= define( source, "day" )
	month	= define( source, "month" )
	year	= define( source, "year" )
	return time.strptime( year+"-"+month+"-"+day, "%Y-%m-%d" )


class SWIFTtransaction:

	def __init__(self, source):

		for field in ["localName", "localAccountNumber", "localBankCode", "remoteName", "remoteAccountNumber", "remoteBankCode", "transactionText", "purpose", "primanota"]:
			self.__dict__[ field ] = define( source, field )

		p = source.find("date {")
		q = source.find("} #date", p)
		self.date = SWIFTdate( source[p:q] )

		p = source.find("valutaDate {")
		q = source.find("} #date", p)	# Ja, "} #date", nicht "} #valutaDate"
		self.valutaDate = SWIFTdate( source[p:q] )

		p = source.find("value {")
		q = source.find("} #value", p)
		if define( source[p:q], "currency" ) != "EUR":
			raise
		self.value = Decimal( define( source[p:q], "value" ).replace("%2F100", "") ) / 100

#		self.transactionCode = ...	# -> Zahlungsweise

class SWIFTresponse:

	def __init__(self, source):

		for field in ["owner", "accountName", "accountNumber", "bankCode", "bankName"]:
			self.__dict__[ field ] = define( source, field )

		p = source.find("transactionList {")
		q = source.find("} #transactionList")
		source = source[p:q]

		self.transactionList = []
		p = source.find("transaction {")
		while ( p > -1 ):
			q = source.find("} #transaction", p)
			self.transactionList.append( SWIFTtransaction(source[p:q]) )
			p = source.find("transaction {", q)

	def UploadToDatabase(self):

		for t in self.transactionList:		# für jede Transaktion
			try:						# gibt es das lokale Konto schon ?
				local = Banking.Bankkonten.objects.using( BankingDB ).get( name=t.localName, kontonummer=t.localAccountNumber, blz=t.localBankCode )
			except:
				Bank = None				# Nein -> speichern
				if t.localBankCode == self.bankCode:
					Bank = self.bankName
				local = Banking.Bankkonten.objects.using( BankingDB ).create( name=t.localName, kontonummer=t.localAccountNumber, bankname=Bank, blz=t.localBankCode )
			
			try:						# gibt es das Konto der Gegenseite schon ?
				remote = Banking.Bankkonten.objects.using( BankingDB ).get( name=t.remoteName, kontonummer=t.remoteAccountNumber, blz=t.remoteBankCode )
			except:
				Bank = None				# Nein -> speichern
				if t.remoteBankCode == self.bankCode:
					Bank = self.bankName
				remote = Banking.Bankkonten.objects.using( BankingDB ).create( name=t.remoteName, kontonummer=t.remoteAccountNumber, bankname=Bank, blz=t.remoteBankCode )

			try:						# gibt es diese exakte Buchung schon ?
				Buchung = Banking.Buchungen.objects.using( BankingDB ).get( bankkonto=local.id, gegenseite=remote.id, datum=t.date, valuta=t.valutaDate, betrag=t.value, primanota=t.primanota, verwendungszweck=t.transactionText+"\n"+t.purpose )
			except:						# Nein -> speichern
				Buchung = Banking.Buchungen.objects.using( BankingDB ).create( bankkonto=local.id, gegenseite=remote.id, datum=t.date, valuta=t.valutaDate, betrag=t.value, primanota=t.primanota, verwendungszweck=t.transactionText+"\n"+t.purpose )


def QueryDKB():
	command = "aqbanking-cli -P input -n request --account=... --transactions"
	SWIFTresponse( Popen( shlex.split(command), stdout=PIPE ).communicate()[0] ).UploadToDatabase()


