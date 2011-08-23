# -*- coding: iso-8859-15 -*-

from banking.python.models import *

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

from datetime import datetime

def Liste( request ):
	params = {}
	params["Konten"] = Bankkonten.objects.all()
	return render_to_response("Konten.html", params)

