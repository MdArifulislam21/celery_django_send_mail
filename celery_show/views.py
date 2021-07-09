from django.shortcuts import render

from django.http import HttpResponse
from .task import *

# Create your views here.
def send_mail_without_celery():
	send_mail('Celery worked Yeah!',
		"celery is cool",
		'arifuldesigner2014@gmail.com',
		['sabuj19977@gmail.com'],
		fail_silently = False
		)
	return None

def index(request):
	send_mail_without_celery()
	print('mail has sent')
	return HttpResponse("<h1> hi man!   hello from celery</h1>")