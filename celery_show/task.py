from celery import shared_task
from time import sleep

from django.core.mail import send_mail


@shared_task
def sleepy(duration):
	sleep(duration)
	return None


@shared_task
def send_to_mail():

	send_mail('wow! Celery worked Yeah!',
		"celery is cool",
		'sabuj19977@gmail.com',
		['arifuldesigner2014@gmail.com'],
		fail_silently = False
		)

	return None