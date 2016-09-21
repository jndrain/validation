from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
	return render(request, "valid/index.html")

def validate(request):
	email = request.POST['email']
	isValid = User.objects.validation(email)
	if isValid:
		messages.success(request, "The email address you entered ({}) is a VALID email address! Thank you!".format(email))
		return redirect('/success')
	else:
		messages.error(request, "Email is not valid!")
		return redirect("/")

def success(request):
	context = {
		"emails": User.objects.all()
	}
	return render(request, "valid/success.html", context)

