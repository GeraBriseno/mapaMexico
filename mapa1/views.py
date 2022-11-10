from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.serializers.json import DjangoJSONEncoder
from .models import Poblacion, PIB
#from .forms import CreateBookShelf
from django.contrib.auth.models import User
import json

def home(response):

    dict_estados_pop = {}
    dict_estados_pib = {}
    estadospop = Poblacion.objects.all()
    estadospib = PIB.objects.all()
    
    for estado in estadospop:
        dict_estados_pop[estado.estado] = [estado.a1910,estado.a1920,estado.a1930,estado.a1940,estado.a1950,estado.a1960,estado.a1970,estado.a1980,estado.a1990,estado.a2000,estado.a2010,estado.a2020]
    
    for estado in estadospib:
        dict_estados_pib[estado.estado] = [estado.a2003,estado.a2004,estado.a2005,estado.a2006,estado.a2007,estado.a2008,estado.a2009,estado.a2010,estado.a2011,estado.a2012,estado.a2013,estado.a2014,estado.a2015,estado.a2016,estado.a2017,estado.a2018,estado.a2019,estado.a2020]
    
    estados_json_pop = json.dumps(dict_estados_pop, cls=DjangoJSONEncoder, ensure_ascii=False)
    estados_json_pib = json.dumps(dict_estados_pib, cls=DjangoJSONEncoder, ensure_ascii=False)
    
    return render(response, "mapa1/home.html", {"estadospop":estados_json_pop, "estadospib":estados_json_pib})