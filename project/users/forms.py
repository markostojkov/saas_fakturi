from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class CreateUserForm(UserCreationForm):

	company = forms.CharField(required=True)

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', 'company')