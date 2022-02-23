from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from regis_proj import settings
from django.core.mail import send_mail





def home(request):
	
	return render(request, "portal/home.html")

def signup(request):
	if request.method == "POST":

		username = request.POST.get('username')

		gname = request.POST.get('gname')

		lname = request.POST.get('lname')

		email = request.POST.get('email')

		cpass = request.POST.get('cpass')

		copass = request.POST.get('copass')


		if User.objects.filter(username=username):
			messages.error(request, "Username already exists, pls try using a different one")
			return redirect('home')

		if User.objects.filter(email=email):
			messages.error(request, "Email already exists")
			return redirect('home')

		if User.objects.filter(password=cpass):
			messages.error(request, "This password is already taken")
			return redirect('home')

		if cpass != copass:
			messages.error(request, 'Passwords are not matching, pls try typing your passwords again')
			return redirect('home')

		myuser = User.objects.create_user(username, email, cpass)

		myuser.first_name = gname

		myuser.last_name = lname 

		myuser.save()

		return redirect('signin')


		






		







	return render(request, "portal/signup.html")

def signin(request):

	



	if request.method == "POST":

		username = request.POST.get('username')

		cpass = request.POST.get('cpass')

		user = authenticate(username=username, password=cpass)



		if user is not None:
			login(request, user)
			gname = user.first_name
			return render(request, "portal/home.html", {'gname' : gname})

		else:
			messages.error(request, "Invalid Credentials")
			return redirect('signup')



		
	return render(request, "portal/signin.html")



def signout(request):
	logout(request)
	messages.success(request, "Logged Out Successfully")
	return redirect('home')


def thankyou(request):
	logout(request)
	return render(request, "portal/thankyou.html")









# Create your views here.
