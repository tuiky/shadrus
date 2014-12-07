from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def basic_one(request):
	view = 'basic_one'
	html = '<html><body><h1>this is %s view </h1></html></body>' % view
	return HttpResponse(html)