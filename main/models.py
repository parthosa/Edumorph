from django.db import models

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
	sc_name = models.CharField(max_length = 100, is_required=True)
	sc_add = models.CharField(max_length=500, is_required=True)
	sc_city = models.ChoiceField(choices=city, is_required=True)
	sc_state = models.ChoiceField(choices=state, is_required=True)
	sc_email = models.EmailField(max_length=50, is_required=True)
	sc_no = models.IntegerField(is_required=True)
	sc_princi = models.CharField(max_length=50, is_required=True)
	sc_auth = models.CharField(max_length=50, is_required=True)
	is_paid = models.BooleanField(default=False)
	enroll_sheet = models.FileField(#path to be written)

	def __str__(self):
			return self.sc_name

class Student(models.Model):
	s School(models.Model):
	city=(
		('Delhi', 'Delhi'),
		#('shit', 'shit'),
		#to be updated
		)
	st_name = models.CharField(max_length = 100, is_required=True)
	st_dob = models.DateField(default=date.now, is_required=True)
	st_city_res = models.CharField(max_length = 20, is_required=True)
	st_city_sc = models.ChoiceField(choices=city, is_required=True)
	st_sc = models.ForeignKey('School', null=False)
	st_email = models.CharField(max_length = 50, is_required=True)
	st_pass = models.PasswordField()

	def __str__(self):
			return self.st_name

