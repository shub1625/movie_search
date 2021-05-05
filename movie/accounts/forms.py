from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from accounts.models import *

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'first_name','last_name','email', 'password1', 'password2']

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        exclude = ['username']
        

