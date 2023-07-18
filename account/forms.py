from django import forms

class UserRegisterationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ali'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'A@gmail.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Enter your password'}))