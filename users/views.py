from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms import RegisterForm,UserUpdate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def home(request):
    return render(request,'users/home.html',{})


def login(request):
    form = AuthenticationForm()
    return render(request,"users/login.html",{"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
				'Welcome !',
				'Good to see you here ! '+str(form.cleaned_data.get('username')),
				'neerajmaurya879@gmail.com',
				[str(form.cleaned_data.get('email'))],
				fail_silently=False
            )
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdate(request.POST, instance=request.user)
		if u_form.is_valid():
			u_form.save()
			return redirect('profile')
	else:
		u_form = UserUpdate()
	context={'u_form':u_form}
	return render(request,'users/profile.html',context)
