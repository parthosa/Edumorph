from django.shortcuts import render
from .models import *

def reg_school(request):
	if request.method == 'POST':
		sc_name = request.POST['sc_name']
		sc_add = request.POST['sc_add']
		sc_city = request.POST['sc_city']
		sc_state = request.POST['sc_state']
		sc_email = request.POST['sc_email']
		sc_no = request.POST['sc_no']
		sc_princi = request.POST['sc_princi']
		sc_auth = request.POST['sc_auth']

	try:
		already_reg = School.objects.get(sc_email=sc_email)
		return render(request, 'main/error.html', {'error_heading' : 'User Already Registered', 'error_message' : 'The email id is already registered.'})	
	except:
		pass
	member = School()	
	try:
		member.user = User.objects.create_user(sc_email, sc_no)	
	except:
		return render(request, main/errors.html)
	member.user.save()
	
	member.sc_name = sc_name
	member.sc_add = sc_add
	member.sc_city = sc_city
	member.sc_email = sc_email
	member.sc_no = sc_no
	member.sc_princi = sc_princi
	member.sc_auth = sc_auth
	member.save()

	#algo for username and psswd to be written

	body = unicode(u'''
		Hi whatever to be filled here to be done by the team


		''')%(#the variables of course)
	send_to = sc_email
	try:
			email = EmailMessage('Application for Registration with TEM', body, 'tem@edumorph.com', [send_to])
			email.attach_file('#path of file on server')
			email.send()
		except:
			return HttpResponse('error')

def reg_st(request):
	if request.method == 'POST':
		st_name = request.POST['st_name']
		st_dob = request.POST['st_dob']
		st_city_res = request.POST['st_city_res']
		st_city_sc = request.POST['st_city_sc']
		st_sc = request.POST['st_sc']
		st_email = request.POST['st_email']
		st_pass = request.POST['st_pass']

	try:
			already_reg = Student.objects.get(st_email=st_email)
			return render(request, 'main/error.html', {'error_heading' : 'User Already Registered', 'error_message' : 'The email id is already registered.'})
	except:
			pass

	member = Student()	
	try:
		member.user = User.objects.create_user(st_email)	
	except:
		return render(request, main/errors.html)
	member.user.save()
	
	member.st_name = st_name
	member.st_dob = st_dob
	member.st_city_res = st_city_res
	member.st_city_sc = st_city_sc
	member.st_email = st_email
	member.st_sc = st_sc
	member.st_pass = st_pass
	member.save()

	#algo for username and psswd to be written

	def gen_username(request):
		c_code = int(member.sc_city) 
		d = []
		today = datetime.date.today()
		d.append(today)
		year = d[0]
		r_year = year[2:]
		s_id = str(member.id)
		u_name = "EM" + r_year + c_code + s_id

		return(u_name)

	def gen_psswd(request):
		psswd = str(member.sc_no)	

		return(psswd)

	def create_user(request):
		user = School.objects.create_user(username=u_name, password=psswd, email_id=member.email_id)	
		member.user = user
		member.save()
		return user

	body = unicode(u'''
		Hi whatever to be filled here to be done by the team


		''')%(#the variables of course)
	send_to = st_email
	try:
			email = EmailMessage('Application for Registration with TEM', body, 'tem@edumorph.com', [send_to])
			email.attach_file('#path of file on server')
			email.send()
		except:
			return HttpResponse('error')		

def sc_dashboard_simple(request):
	response = {'name': School.sc_name,
				'address': School.sc_add,
				'city': School.city,
				'state': School.state,
				'email_id': School.email_id,
				'phone_no': School.phone_no,
				'princi_name': School.sc_princi,
				'auth_name': School.sc_name,
	}
	return JsonResponse(response)

def sc_dashboard_file(request):
	#to be written

def sc_dashboard_payment(request):
	#to be written

def sc_dashboard_status(request):
	if School.enroll_sheet = null:
		response = {'paid' = School.is_paid,
					'registered' = True,
					'enroll_sheet': False,
					'enroll_aknowledge': #pata nahi bc,
					'roll_generate': #to be asked,
					'exam_conduct': #to be asked,
		}	
	else:
		response = {'paid' = School.is_paid,
					'registered' = True,
					'enroll_sheet': True,
					'enroll_aknowledge': #pata nahi bc,
					'roll_generate': #to be asked,
					'exam_conduct': #to be asked,
		}			
	return JsonResponse(response)	

def sc_dashboard_roll(request):
	#if roll numbers not generated:
	response = {'status' = 0,
				'message' = PLEASE BE PATIENT WHILE WE FINISH THE PROCEDURES.,
	}	
	#else:
	#response = {'status' = 0,
	#			'message' = Click the link below to download the roll numbers
	#}
 	return JsonResponse(response)

def sc_edit(request):
	if request.method == 'POST':
		sc_add = request.POST['sc_add']
		sc_city = request.POST['sc_city']
		sc_state = request.POST['sc_state']
		sc_email = request.POST['sc_email']
		sc_no = request.POST['sc_no']
		sc_princi = request.POST['sc_princi']
		sc_auth = request.POST['sc_auth']
		#I guess it would be good to add a separate link for changing password

	try:
		member = School()
		member.sc_add = sc_add
		member.sc_city = sc_city
		member.sc_email = sc_email
		member.sc_no = sc_no
		member.sc_princi = sc_princi
		member.sc_auth = sc_auth
		member.save()

		response = {'status': 1,
					'message': Your information was saved successfully,
		}

	except:
		response = {'status': 0,
					'message': error
		}

	return JsonResponse(response)	
