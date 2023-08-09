from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Relation

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
            return redirect('home:home')
        return render(request, self.template_name, {'form': form})
class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'account/login.html'

    def setup(self, request, *args, **kwargs):
        self.next = request.GET.get('next', None)
        return super().setup(request,*args,**kwargs)


    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.error(request, 'you are login', 'warning')
            return redirect('home:home')
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
                if self.next:
                    return redirect('home:home')
                return redirect('home:home')
        messages.error(request, 'username or password is wrong', 'danger')
        return render(request, self.template_name, {'form': form})

class UserLogoutView(LoginRequiredMixin, View):
    login_url = '/account/login/'
    def get(self, request):
        logout(request)
        messages.success(request, 'you logout succesfuly', 'success')
        return redirect('home:home')

class UserProfileView(LoginRequiredMixin,View):
    def get(self, request, user_id):
        is_following = False
        user = User.objects.get(pk=user_id)
        post = user.posts.all()
        relation = Relation.objects.filter(from_user=request.user, to_user=user)
        if relation.exists():
            is_following = True
        return render(request, 'account/profile.html', {'user':user, 'is_following':is_following,})

class UserPostView(LoginRequiredMixin,View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        post = user.posts.all()
        return render(request, 'account/Posts.html', {'user':user, 'post':post,})

class UserFllowersView(LoginRequiredMixin,View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        follow=Relation.objects.all()
        return render(request, 'account/followers.html', {'user':user, 'follow':follow})

class UserFllowingView(LoginRequiredMixin,View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        follow=Relation.objects.all()
        return render(request, 'account/following.html', {'user':user, 'follow':follow})


class UserFollowView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        relation = Relation.objects.filter(from_user=request.user, to_user=user)
        if relation.exists():
            messages.error(request, 'you are already following this user', 'danger')
        else:
            Relation.objects.create(from_user=request.user, to_user=user).save()
            messages.success(request, 'you followed this user', 'success')
        return redirect('user_profile', user_id)


class UserUnFollowView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        relation = Relation.objects.filter(from_user=request.user, to_user=user)
        if relation.exists():
            relation.delete()
            messages.success(request, 'you unfollowed this user', 'success')
        else:
            messages.error(request, 'you are not following this user', 'danger')
        return redirect('user_profile', user_id)