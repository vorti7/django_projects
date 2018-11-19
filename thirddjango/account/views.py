from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from account.forms import ProfileForm

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('question:index')
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('question:index')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form':form})

def logout(request):
    auth_logout(request)
    return redirect('question:index')

def signup(request):
    if request.method == "POST":
        form = UsercreatinForm(request.POST)
        pro_form = ProfileForm(request.POST)
        if form.is_valid() and pro_form.is_valid():
            user = form.save()
            profile = pro_form.save(commit=False)
            profile.user = user
            pro_form.save()
            auth_login(request, user)
            return redirect('question:index')
    else:
        form = UserCreationForm()
        pro_form = ProfileForm()
    return render(request, 'account/signup.html', {'form':form, 'pro_form':pro_form})