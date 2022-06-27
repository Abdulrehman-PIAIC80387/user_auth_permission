from django import forms

from mobile_app.models import person
from .models import *

from django.forms import ModelForm

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class InvoiceForm(forms.ModelForm):
	class Meta:
		model = person
		fields = ['person_name', 'address','age', 'date',
				'address','hotel_Main_Img',
				]
		widgets = {
            'date': DateInput(),
        }


class InvoiceUpdateForm(forms.ModelForm):
	class Meta:
		model = person
		fields = ['person_name', 'address','age', 'date',
				'address','hotel_Main_Img',
				]
		widgets = {
            'date': DateInput(),
        }

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


		