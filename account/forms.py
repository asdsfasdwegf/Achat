from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegisterationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confrim_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('this email already exists')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('this username already exists')
        return username
    def clean(self):
        cd = super().clean()
        p1 = cd.get('password')
        p2 = cd.get('confrim_password')
        if p1 and p1 and p1 != p2:
            raise ValidationError('password are not match')

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username or Email',widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

