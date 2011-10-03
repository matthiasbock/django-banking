# -*- coding: iso-8859-15 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from Django.banking.models import *

def Start( request ):
	return HttpResponseRedirect("Buchungen/")

def Liste( request ):
	params = {}
	params["Buchungen"] = []

	for B in Buchungen.objects.using( BankingDB ).all().order_by("-datum"):
		b			= {}
		b["id"]			= B.id
		Bankkonto		= Bankkonten.objects.using( BankingDB ).get( id=B.bankkonto )
		b["bankkonto"]		= Bankkonto.name+"<br/>Kontonummer: "+str( Bankkonto.kontonummer )+"<br/>IBAN: "+Bankkonto.iban+"<br/>"+str( Bankkonto.blz )+" "+Bankkonto.kreditinstitut+"<br/>BIC: "+Bankkonto.bic
		Bankkonto		= Bankkonten.objects.using( BankingDB ).get( id=B.gegenseite )
		b["gegenseite"]		= Bankkonto.name+"<br/>Kontonummer: "+str( Bankkonto.kontonummer )+"<br/>IBAN: "+Bankkonto.iban+"<br/>"+str( Bankkonto.blz )+" "+Bankkonto.kreditinstitut+"<br/>BIC: "+Bankkonto.bic
		b["datum"]		= B.datum
		b["valuta"]		= B.valuta
		b["betrag"]		= B.betrag
		b["primanota"]		= str( B.primanota )
		b["verwendungszweck"]	= B.verwendungszweck

		params["Buchungen"].append( b )

	return render_to_response("Buchungen.html", params)


def HBCI_Query( request ):
	QueryDKB()
	return HttpResponseRedirect(".")


def CSV_Upload( request ):

	if request.method == "GET":
		return render_to_response("UploadCSV.html", {})

	elif request.method == "POST":

		# Importiere eine CSV im Format der Berliner Sparkasse:	
		#	"Buchungsdatum";"Valuta";"Betrag";"Währung";"Empfängername1";"Empfängername2";"Primanota";"BLZ/BIC Empfänger";
		# 	"Kontonummer/IBAN Empfänger";"Verwendungszweck 1";"Verwendungszweck 2";"Verwendungszweck 3";"Verwendungszweck 4";
		# 	"Verwendungszweck 5";"Verwendungszweck 6";"Verwendungszweck 7";"Verwendungszweck 8";"Verwendungszweck 9";"Verwendungszweck 10"

		CSV = request.FILES['CSV'].replace('"','').split("\n")
		nr = 1
		end = False
		for line in CSV:			# Zeile für Zeile ...
			if line == "":
				end = True
			elif nr > 1 and not end:
				line = line.split(";")	# Spalte für Spalte ...
				Gegenseite = 0
				if line[8] != "":				# Kontonummer oder IBAN vorhanden ?
					try:
						Kontonummer = long( line[8] )	# schlägt fehl bei IBANs, denn IBANs enthalten Buchstaben
						IBAN = False
					except:
						Kontonummer = 0
						IBAN = True
					if IBAN:				# kennen wir das Konto der Gegenseite schon ?
						IBAN = line[8]
						BIC = line[7]
						BLZ = 0
						try:
							Gegenseite = Bankkonten.objects.using( BankingDB ).get( iban=IBAN )
						except:
							Gegenseite = None
					else:
						IBAN = ""
						BIC = ""
						BLZ = line[7]
						try:
							Gegenseite = Bankkonten.objects.using( BankingDB ).get( kontonummer=Kontonummer )
						except:
							Gegenseite = None
					if Gegenseite == None:			# Gegenseite ist unbekannt -> Kontodaten speichern
						Name = line[4]
						Zusatz = line[5]
						Kreditinstitut = ""
						Gegenseite = Bankkonten.objects.using( BankingDB ).create( name=Name, zusatz=Zusatz, kontonummer=Kontonummer, blz=BLZ, bic=BIC, kreditinstitut=Kreditinstitut, iban=IBAN )
					Gegenseite = Gegenseite.id
				else:						# keine Kontonummer oder IBAN angegeben
					Gegenseite = 0
				Verwendungszweck = ""				# Verwendungszweck
				for i in range(9,19):
					Verwendungszweck = Verwendungszweck+line[i]+"\n"
				d = line[0].split(".")
				Buchungsdatum = "20"+d[2]+"-"+d[1]+"-"+d[0]	# Datum
				d = line[1].split(".")
				Valuta = "20"+d[2]+"-"+d[1]+"-"+d[0]		# Wertstellung

				try:						# ist es eine schon bekannte Buchung ?
					Buchungen.objects.using( BankingDB ).get( bankkonto=Bankkonten.objects.using( BankingDB ).get( kontonummer=KtoNr ).id, gegenseite=Gegenseite, buchungsdatum=Buchungsdatum, valuta=Valuta, betrag=line[2].replace(",","."), primanota=line[6], verwendungszweck=Verwendungszweck )
				except:						# Nein -> speichern
					Buchungen.objects.using( BankingDB ).create( bankkonto=Bankkonten.objects.using( BankingDB ).get( kontonummer=KtoNr ).id, gegenseite=Gegenseite, buchungsdatum=Buchungsdatum, valuta=Valuta, betrag=line[2].replace(",","."), primanota=line[6], verwendungszweck=Verwendungszweck )
			nr += 1

		return HttpResponseRedirect(".")

