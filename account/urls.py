from django.urls import path
from . import views

urlpatterns =[
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('profile/<int:user_id>/', views.UserProfileView.as_view(), name='user_profile'),
    path('follow/<int:user_id>/', views.UserFollowView.as_view(), name='user_follow'),
    path('unfollow/<int:user_id>/', views.UserUnFollowView.as_view(), name='user_unfollow'),
    path('Posts/<int:user_id>/', views.UserPostView.as_view(), name='user_Posts'),
    path('followers/<int:user_id>/', views.UserFllowersView.as_view(), name='user_followers'),
    path('following/<int:user_id>/', views.UserFllowingView.as_view(), name='user_following'),
]