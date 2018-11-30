from django import forms
from django.contrib.auth.models import User
import re


class RegistrationForm(forms.Form):
	eId = forms.CharField(label='工号',max_length=30)
	username = forms.CharField(label='账号', max_length=50)
	password1 = forms.CharField(label='密码', widget=forms.PasswordInput(attrs={"placeholder":"请输入密码"}))
	password2 = forms.CharField(label='密码', widget=forms.PasswordInput(attrs={"placeholder":"请再次输入密码"}))
	flag = forms.IntegerField(label='标识')
	
	# Use clean methods to define custom validation rules

	def clean_username(self):
		username = self.cleaned_data.get('username')

		if len(username) < 6:
			raise forms.ValidationError("Your username must be at least 6 characters long.")
		elif len(username) > 50:
			raise forms.ValidationError("Your username is too long.")
		else:
			filter_result = User.objects.filter(username__exact=username)
			if len(filter_result) > 0:
				raise forms.ValidationError("Your username already exists.")
		return username

	def clean_password1(self):
		password1 = self.cleaned_data.get('password1')

		if len(password1) < 6:
			raise forms.ValidationError("Your password is too short.")
		elif len(password1) > 20:
			raise forms.ValidationError("Your password is too long.")
		return password1

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Password mismatch. Please enter again.")
		return password2


