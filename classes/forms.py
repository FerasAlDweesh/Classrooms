from django import forms
from .models import Classroom
from django.contrib.auth.models import User

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = '__all__'

class RegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username", "password", "first_name", "last_name"]

		widgets={
        'password': forms.PasswordInput(),
        }

class LoginForm(forms.ModelForm):
	username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

