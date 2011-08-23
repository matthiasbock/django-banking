# -*- coding: iso-8859-15 -*-

from banking.python.models import *

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

from datetime import datetime

def Liste( request ):
	params = {}
	params["Quittungen"] = []
	for Q in Quittungen.objects.all():
		params["Quittungen"].append({ "id":Q.id, "aussteller":Quittungsaussteller.objects.get( id=Q.aussteller ), "datum":Q.datum, "konto":Bankkonten.objects.get( id=Q.konto ), "betrag":Q.betrag, "zahlungsweise":Zahlungsweisen.objects.get( id=Q.zahlungsweise ).name, "kategorie":Quittungskategorien.objects.get( id=Q.kategorie ).name, "kommentar":Q.kommentar, "buchung":Q.buchung })
	return render_to_response("Quittungen.html", params)

def Neu( request ):
	params = {}
	if request.method == "GET":
		params["Aussteller"] = Quittungsaussteller.objects.all()
		params["Bankkonten"] = Bankkonten.objects.all()
		params["Zahlungsweisen"] = Zahlungsweisen.objects.all()
		params["Kategorien"] = Quittungskategorien.objects.all()
		return render_to_response("NeueQuittung.html", params)
	else:
		Datum = request.POST.get("Tag")+"."+request.POST.get("Monat")+"."+request.POST.get("Jahr")+" "+request.POST.get("Stunde")+":"+request.POST.get("Minute")
		Betrag = float( int(request.POST.get("VorKomma")) + int(request.POST.get("NachKomma"))/(10.**len(request.POST.get("NachKomma"))) )
		Quittungen.objects.create( aussteller=int(request.POST.get("Aussteller")), datum=datetime.strptime( Datum, "%d.%m.%Y %H:%M" ), konto=int(request.POST.get("Konto")), betrag=Betrag, zahlungsweise=int(request.POST.get("Zahlungsweise")), kategorie=int(request.POST.get("Kategorie")) )
		return HttpResponseRedirect("Quittungen")
