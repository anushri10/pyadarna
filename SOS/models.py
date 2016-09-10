import datetime 
from django.db import models

class Memberdata(models.Model):
	UUID = models.IntegerField()
	first_name = models.CharField(max_length=50)
	last_name= models.CharField(max_length=50)
	dob = models.DateTimeField('Date of birth: ')
	sex = models.CharField('F/M: ', max_length=1)
	batch = models.IntegerField('Batch: ')
	sap_id = models.IntegerField('SAP ID: ')
	div = models.CharField('Division: ',max_length=5)
	year = models.IntegerField('Year: ')
	course = models.CharField('Course: ',max_length=20)
	stream = models.CharField('Stream: ',max_length=10)
	email = models.CharField('email: ',max_length=50)
	phone = models.IntegerField('phone number: ')
	address = models.CharField('Address: ',max_length=200)


	
		
