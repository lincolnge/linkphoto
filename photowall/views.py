from django.shortcuts import render_to_response
from django.template import Template
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime

def index(request):
    return render_to_response('index.html', {"value":"hellowrold"})
