from django.shortcuts import render,redirect
from .models import User,Member,Chairman,Watchman,Visitors,Event,Notice
from django.conf import settings
from django.core.mail import send_mail
import random
from django.http import JsonResponse

# Create your views here.
def index(request):
	return render(request,'index.html')

def signup(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			msg1 = "email alredy exist..."
			return render(request,'signup.html',{'msg1':msg1})
		except:
			if request.POST['pswd'] == request.POST['cpswd']:
				user=User.objects.create(
					name=request.POST['name'],
					email=request.POST['email'],
					pswd=request.POST['pswd'],
					)
				msg="signup successfuly..."
				return render(request,'login.html',{'msg':msg})
			else:
				msg1="password and confirm password are not matched...."
				return render(request,'signup.html',{'msg1':msg1})
	else:
		return render(request,'signup.html')

def e_verify(request):
	email=request.GET.get('email')
	print(">>>>>>>>>>>>>>>>AJAX DATA : ",email)
	data={'is_taken':User.objects.filter(email__iexact=email).exists()}
	return JsonResponse(data)


def login(request):
	if request.method=='POST':
		try:
			user=User.objects.get(email=request.POST['email'],pswd=request.POST['pswd'])
			msg="Login successfully.."
			request.session['email']=user.email
			request.session['pswd']=user.pswd
			return render(request,'index.html')
		except:
			msg1="email doesn't exist..."
			return render(request,'login.html',{'msg1':msg1})
	else:
		return render(request,'login.html') 

def logout(request):
	del request.session['email']
	return redirect('login')

def fpswd(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])

			subject = 'Forgot Password OTP'
			otp=random.randint(1000,9999)
			message = f'Hi {user.name}, thank you for registering in MyApp. Your OTP is :{otp}'
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email, ]
			send_mail( subject, message, email_from, recipient_list )
			return render(request,'verify_otp.html',{'email':user.email,'otp':str(otp)})
		except:
			msg1 ="you are not a registered user..."
			return render(request,'fpswd.html',{'msg1':msg1})

	else:
		return render(request,'fpswd.html')

def verify_otp(request):
	if request.method=="POST":
		email=request.POST['email']
		otp=request.POST['otp']
		uotp=request.POST['uotp']

		if uotp == otp:
			return render(request,'set_pswd.html',{'email':email})
		else:
			msg1="OTP does not matched.."
			return render(request,'verify_otp.html',{'msg1':msg1})
	else:
		return render(request,'verify_otp.html')

def set_pswd(request):
	if request.method=="POST":
		email=request.POST['email']
		npswd=request.POST['npswd']
		cnpswd=request.POST['cnpswd']

		if npswd==cnpswd:
			user=User.objects.get(email=email)
			user.pswd=npswd
			user.save()
			return redirect('login')
		else:
			msg1 = "password and confirm password both are not matched..."
			return render(request,'set_pswd.html',{'msg1':msg1})

	else:
		return render(request,'set_pswd.html')

def add_members(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])

		Member.objects.create(
			user=user,
			m_name=request.POST['m_name'],
			m_contact=request.POST['m_contact'],
			m_num=request.POST['m_num'],
		)
		msg="member added successfully..."
		return render(request,'add_members.html',{'msg':msg})
	else:
		return render(request,'add_members.html')

def members(request):
	seller=User.objects.get(email=request.session['email'])
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>by method",seller)
	member=Member.objects.filter(user=seller)
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",member)
	return render(request,'members.html',{'member':member})

def update_members(request,pk):
	seller=User.objects.get(email=request.session['email'])
	member=Member.objects.get(pk=pk,user=seller)
	if request.method=="POST":
		member.user=seller
		member.m_name=request.POST['m_name']
		member.m_contact=request.POST['m_contact']
		member.m_num=request.POST['m_num']
		member.save()
		return render(request,'members.html',{'member':member})
	else:
		return render(request,'update_members.html',{'member':member})

def delete_members(request,pk):
	seller=User.objects.get(email=request.session['email'])
	member=Member.objects.get(pk=pk,user=seller)

	member.delete()
	return redirect("index")

def add_chairmans(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])

		Chairman.objects.create(
			user=user,
			c_name = request.POST['c_name'],
			c_contact = request.POST['c_contact'],
		)
		msg="chairman added successfully..."
		return render(request,'add_chairmans.html',{'msg':msg})
	else:
		return render(request,'add_chairmans.html')

def chairmans(request):
	c=User.objects.get(email=request.session['email'])
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>by method",c)
	chairman=Chairman.objects.filter(user=c)
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",chairman)
	return render(request,'chairmans.html',{'chairman':chairman})

def update_chairmans(request,pk):
	c=User.objects.get(email=request.session['email'])
	chairman=Chairman.objects.get(pk=pk,user=c)
	if request.method=="POST":
		chairman.user=c
		chairman.c_name=request.POST['c_name']
		chairman.c_contact=request.POST['c_contact']
		chairman.save()
		return render(request,'chairmans.html',{'chairman':chairman})
	else:
		return render(request,'update_chairmans.html',{'chairman':chairman})

def delete_chairmans(request,pk):
	c=User.objects.get(email=request.session['email'])
	chairman=Chairman.objects.get(pk=pk,user=c)

	chairman.delete()
	return redirect("index")

def add_watchmans(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])

		Watchman.objects.create(
			user=user,
			w_name = request.POST['w_name'],
			w_contact = request.POST['w_contact'],
		)
		msg="watchman added successfully..."
		return render(request,'add_watchmans.html',{'msg':msg})
	else:
		return render(request,'add_watchmans.html')

def watchmans(request):
	w=User.objects.get(email=request.session['email'])
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>by method",w)
	watchman=Watchman.objects.filter(user=w)
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",watchman)
	return render(request,'watchmans.html',{'watchman':watchman})

def update_watchmans(request,pk):
	w=User.objects.get(email=request.session['email'])
	watchman=Watchman.objects.get(pk=pk,user=w)
	if request.method=="POST":
		watchman.user=w
		watchman.w_name=request.POST['w_name']
		watchman.w_contact=request.POST['w_contact']
		watchman.save()
		return render(request,'watchmans.html',{'watchman':watchman})
	else:
		return render(request,'update_watchmans.html',{'watchman':watchman})

def delete_watchmans(request,pk):
	w=User.objects.get(email=request.session['email'])
	watchman=Watchman.objects.get(pk=pk,user=w)

	watchman.delete()
	return redirect("index") 

def add_visitors(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])

		Visitors.objects.create(
			user=user,
			v_name = request.POST['v_name'],
			v_contact = request.POST['v_contact'],
		)
		msg="visitors added successfully..."
		return render(request,'add_visitors.html',{'msg':msg})
	else:
		return render(request,'add_visitors.html')

def visitors(request):
	d=User.objects.get(email=request.session['email'])
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>by method",d)
	visitor=Visitors.objects.filter(user=d)
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",visitor)
	return render(request,'visitors.html',{'visitor':visitor})

def update_visitors(request,pk):
	d=User.objects.get(email=request.session['email'])
	visitor=Visitors.objects.get(pk=pk,user=d)
	if request.method=="POST":
		visitor.user=d
		visitor.v_name=request.POST['v_name']
		visitor.v_contact=request.POST['v_contact']
		visitor.save()
		return render(request,'update_visitors.html',{'visitor':visitor})
	else:
		return render(request,'update_visitors.html',{'visitor':visitor})

def delete_visitors(request,pk):
	d=User.objects.get(email=request.session['email'])
	visitor=Visitors.objects.get(pk=pk,user=d)

	visitor.delete()
	return redirect("index") 

def add_events(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])

		Event.objects.create(
			user=user,
			e_name = request.POST['e_name'],
			e_date = request.POST['e_date'],
		)
		msg="event added successfully..."
		return render(request,'add_events.html',{'msg':msg})
	else:
		return render(request,'add_events.html')

def events(request):
	e=User.objects.get(email=request.session['email'])
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>by method",e)
	event=Event.objects.filter(user=e)
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",event)
	return render(request,'events.html',{'event':event})

def update_events(request,pk):
	e=User.objects.get(email=request.session['email'])
	event=Event.objects.get(pk=pk,user=e)
	if request.method=="POST":
		event.user=e
		event.e_name=request.POST['e_name']
		event.e_date=request.POST['e_date']
		event.save()
		return render(request,'update_events.html',{'event':event})
	else:
		return render(request,'update_events.html',{'event':event})

def delete_events(request,pk):
	e=User.objects.get(email=request.session['email'])
	event=Event.objects.get(pk=pk,user=e)

	event.delete()
	return redirect("index")

def add_notices(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])

		Notice.objects.create(
			user=user,
			n_name = request.POST['n_name'],
			n_sub = request.POST['n_sub'],
		)
		msg="notice added successfully..."
		return render(request,'add_notices.html',{'msg':msg})
	else:
		return render(request,'add_notices.html')

def notices(request):
	notices=User.objects.get(email=request.session['email'])
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>by method",notices)
	notice=Notice.objects.filter(user=notices)
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",notice)
	return render(request,'notices.html',{'notice':notice})

def update_notices(request,pk):
	notices=User.objects.get(email=request.session['email'])
	notice=Notice.objects.get(pk=pk,user=notices)
	if request.method=="POST":
		notice.user=seller
		notice.n_name=request.POST['n_name']
		notice.n_sub=request.POST['n_sub']
		notice.save()
		return render(request,'update_notices.html',{'notices':notices})
	else:
		return render(request,'update_notices.html',{'notices':notices})

def delete_notices(request,pk):
	notices=User.objects.get(email=request.session['email'])
	notice=Notice.objects.get(pk=pk,user=notices)

	notices.delete()
	return redirect("index")