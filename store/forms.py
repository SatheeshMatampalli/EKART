from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from account.models import CourseInfo
from store.models import *
from django import forms

class UserSignupForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email']


class AddProductForm(ModelForm):
	class Meta:
		model=Product
		fields='__all__'
