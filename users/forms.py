from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'phone', 'email', 'password1', 'password2']

class UserUpdate(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email']
