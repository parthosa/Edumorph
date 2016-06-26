from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators.csrf import csrf_exempt

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

	student = Student()	
	try:
		student.user = User.objects.create_user(st_email)	
	except:
		return render(request, main/errors.html)
	student.user.save()
	
	student.st_name = st_name
	student.st_dob = st_dob
	student.st_city_res = st_city_res
	student.st_city_sc = st_city_sc
	student.st_email = st_email
	student.st_sc = st_sc
	student.st_pass = st_pass
	student.save()

	#algo for username and psswd to be written

def gen_username(request):
	c_code = int(student.sc_city) 
	d = []
	today = datetime.date.today()
	d.append(today)
	year = d[0]
	r_year = year[2:]
	s_id = str(student.id)
	u_name = "EM" + r_year + c_code + s_id

	return(u_name)

def gen_psswd(request):
	psswd = str(student.sc_no)	

	return(psswd)

def create_user(request):
	student = User.objects.create_user(username=u_name, password=psswd, email_id=student.st_email)	
	student.save()
	return student

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

@csrf_exempt
def user_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
					login(request, user)
					return HttpResponseRedirect('../dashboard/',)
			else:
				response = {'error_heading' : "Account Inactive", 'error_message' :  'Your account is currently INACTIVE. To activate it, call the following members of the Department of Publications and Correspondence depending on the region of your college.<br> <strong> North India :- Ankit Dube | +91 9983083610 </strong> <br> <strong>Delhi/NCR :- Aditya Shetty :- +91 7240105157 </strong><br><strong>Central India :- Poonam Brar | +91 7240105158 </strong><br><strong>Rajasthan, Gujarat & Maharashtra :- Karthik Maddipoti | +91 8003193680 </strong><br><strong>East India :- Tanhya Chitle | +91 7240105155 </strong><br><strong>South India :- Archana Tatavarti |+91 7240105150 </strong><br />Return back <a href="/">home</a>'}
				return JsonResponse(response)
		else:
			response = {'error_heading' : "Invalid Login Credentials", 'error_message' :  'Please'}
			return JsonResponse(response)
	else:
		return render(request, 'registrations/login.html')	

@login_required
def user_logout(request):
	user = request.user;
	logout(request)					

@login_required
def sc_dashboard_simple(request):
	school = School.objects.get(request.user.sc_email)

	response = {'name': school.sc_name,
				'address': school.sc_add,
				'city': school.city,
				'state': school.state,
				'email_id': school.email_id,
				'phone_no': school.phone_no,
				'princi_name': school.sc_princi,
				'auth_name': school.sc_name,
	}
	return JsonResponse(response)

@login_required
def sc_dashboard_file(request):
	#to be written

@login_required
def sc_dashboard_payment(request):
	school = School.objects.get(request.user.sc_email)

	if school.is_paid == True:
		response={'message' = You have paid}

	else:
		response = {'message' = Kindly follow the link to make your payment }

	return JsonResponse(response)	

@login_required
def sc_dashboard_status(request):
	school = School.objects.get(request.user.sc_email)

	if school.enroll_sheet = null:
		response = {'paid' = school.is_paid,
					'registered' = True,
					'enroll_sheet': False,
					'enroll_aknowledge': #pata nahi bc,
					'roll_generate': #to be asked,
					'exam_conduct': #to be asked,
		}	
	else:
		response = {'paid' = school.is_paid,
					'registered' = True,
					'enroll_sheet': True,
					'enroll_aknowledge': #pata nahi bc,
					'roll_generate': #to be asked,
					'exam_conduct': #to be asked,
		}			
	return JsonResponse(response)	

@login_required
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

@login_required
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

###########################################Payment Gateway###########################################################################
from paypal.standard.ipn import PayPalPaymentsForm

def main_pay(request):

    paypal_dict = {
        "business": #paypal id,
        "amount": #to be asked,
        "item_name": "Registration with Edumorph",
        "invoice": "unique-invoice-id",
        "notify_url": "https://www.example.com" + reverse('paypal-ipn'),
        "return_url": "https://www.edumorph.com/thank_you/",
        "cancel_return": "https://www.edumorph.com/oops/",
        "callback_timeout": "3",
        "custom": "Upgrade all users!",  # Custom command to correlate to some function later (optional)
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "payment.html", context)
