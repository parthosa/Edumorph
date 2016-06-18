from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class School(models.Model):
		city=(
			('Delhi', 'Delhi'),
			#('shit', 'shit'),
			#to be updated
			)
		state=(
			('Delhi', 'Delhi'),
			#('shit', 'shit'),
			#to be updated
			)
		user = models.OneToOneField(User, null=True)
		sc_name = models.CharField(max_length = 100)
		sc_add = models.CharField(max_length=500)
		sc_city = models.CharField(max_length=30,choices=city)
		sc_state = models.CharField(max_length=30,choices=state)
		sc_email = models.EmailField(max_length=50)
		sc_no = models.IntegerField()
		sc_princi = models.CharField(max_length=50)
		sc_auth = models.CharField(max_length=50)
		is_paid = models.BooleanField(default=False)
		enroll_sheet = models.FileField()

class Student(models.Model):
		city=(
			('Delhi', 'Delhi'),
			#('shit', 'shit'),
			#to be updated
			)
		user = models.OneToOneField(User, null=True)
		st_name = models.CharField(max_length = 100)
		st_dob = models.DateField(auto_now=True)
		st_city_res = models.CharField(max_length = 20)
		st_city_sc = models.CharField(max_length=30,choices=city)
		st_sc = models.ForeignKey('School', null=False)
		st_email = models.CharField(max_length = 50)
		st_pass = models.CharField(max_length=30)

		def __str__(self):
				return self.st_name



