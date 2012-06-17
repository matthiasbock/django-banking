# -*- coding: iso-8859-15 -*-
#!/usr/bin/python

import time
from decimal import *

def extract_field(source, field):
	field	= ' '+field.replace('", "', '\n')+'="'
	p	= source.find( field )
	if p > -1:
		p += len( field )
	else:
		return ""
	q	= source.find('"', p)
	return source[p:q]

def parse_date( text ):
	day	= extract_field( text, "day" )
	month	= extract_field( text, "month" )
	year	= extract_field( text, "year" )
	return time.strptime( year+"-"+month+"-"+day, "%Y-%m-%d" )

class transaction:
	def __init__(self, source):
		for field in ["localName", "localAccountNumber", "localBankCode", "remoteName", "remoteAccountNumber", "remoteBankCode", "transactionText", "purpose", "primanota"]:
			self.__dict__[ field ] = extract_field( source, field )

		p = source.find("date {")
		q = source.find("} #date", p)
		self.date = parse_date( source[p:q] )

		p = source.find("valutaDate {")
		q = source.find("} #date", p)		# not a mistake, it really is "} #date" not "} #valutaDate"
		self.valutaDate = parse_date( source[p:q] )

		p = source.find("value {")
		q = source.find("} #value", p)

		if extract_field( source[p:q], "currency" ) != "EUR":
			print "Currency is not Euro. Fatal!"
			raise

		self.value = Decimal( extract_field(source[p:q], "value").replace("%2F100", "") ) / 100

#		self.transactionCode = ...		# -> Zahlungsweise

class accountInfo:
	def __init__(self, source):
		for field in ["owner", "accountName", "accountNumber", "bankCode", "bankName"]:
			self.__dict__[ field ] = extract_field( source, field )

		p = source.find("transactionList {")
		q = source.find("} #transactionList")
		source = source[p:q]			# my only interest is the transaction list, I don't care about this whole status etc crap

		self.transactionList = []
		p = source.find("transaction {")
		while ( p > -1 ):
			q = source.find("} #transaction", p)
			self.transactionList.append( transaction(source[p:q]) )
			p = source.find("transaction {", q)

class accountInfoList:
	def __init__(self, source):
		self.accountInfo = []
		p = source.find("accountInfo {")
		while ( p > -1 ):
			q = source.find("} #accountInfo", p)
			self.accountInfo.append( accountInfo(source[p:q]) )
			p = source.find("accountInfo {", q)

class HBCI_response:
	def __init__(self, filename):
		self.accountInfoList = accountInfoList( open(filename).read() )

