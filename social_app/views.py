from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from verify_email.email_handler import send_verification_email
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

def index(request):
  return render(request, 'index.html')

def signup(request):
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    if password == password2:
      if User.objects.filter(email=email).exists():
        messages.info(request, 'Email already exists')
        return redirect('signup')
      elif User.objects.filter(username=username).exists():
        messages.info(request, 'Username already exists')
        return redirect('signup')
      else:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_active = False
        user.save()

        return redirect('login')
    else:
      messages.info(request, 'Passwords do not match')
      return redirect('signup')
  else: 
    return render(request, 'signup.html')
  

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
      auth.login(request, user)
      return redirect('/')
    else:
      messages.info(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'login.html')

def logout(request):
  auth.logout(request)
  return redirect('index')

@login_required
def create_or_update_profile(request):
  if request.method == 'POST':
    form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)