from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


class UserRegisterView(View):
    form_class = UserRegisterationForm
    template_name = 'account/register.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.error(request, 'you are login', 'warning')
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        form = UserRegisterationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request, 'your account created', 'success')
            return redirect('home')
        return render(request, self.template_name, {'form': form})
class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'account/login.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.error(request, 'you are login', 'warning')
            return redirect('home')
        return super().dispatch(request,*args, **kwargs)
    def get(self, request):
        form = self.form_class()
        form = UserLoginForm()
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'your are login', 'success')
                return redirect('home')
        messages.error(request, 'username or password is wrong', 'danger')
        return render(request, self.template_name, {'form': form})

class UserLogoutView(LoginRequiredMixin, View):
    login_url = '/account/login/'
    def get(self, request):
        logout(request)
        messages.success(request, 'you logout succesfuly', 'success')
        return redirect('home')

class UserProfileView(LoginRequiredMixin,View):
    def get(self, request, user_id):
        user = User.objects.get(id = user_id)
        return render(request, 'account/profile.html', {'user':user})
