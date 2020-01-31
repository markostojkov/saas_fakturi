from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from company.models import Company
from .models import User
from .forms import CreateUserForm


def register(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		company = request.POST.get('company')
		username = request.POST.get('username')
		password = request.POST.get('password1')
		try:
			company = Company.objects.create(name=company)
		except Exception:
			messages.error(request, 'Компанија со ова име постои')
			return redirect('register')
		User.objects.create(username=username, password=password, company=company)
		messages.success(request, 'Успешно')
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect('homepage')

	context = {
		'form': form
	}

	return render(request, 'users/register.html', context)
