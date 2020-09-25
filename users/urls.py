from django.urls import path
from .views import home, login, register, profile, logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home,name="home"),
    #path('login/', login,name="login"), 
    path('Register/', register,name="register"),
    path('profile/',profile,name="profile"),
    #path('logout',logout,name="logout"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),# Using builtIn method
    path('logout/', auth_views.LoginView.as_view(template_name='users/logout.html'),name='logout'),
]