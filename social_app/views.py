from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse
from verify_email.email_handler import send_verification_email
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, Like, Comment
from .forms import ProfileForm, PostForm, CommentForm

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

    user = auth.authenticate(request, username=username, password=password)

    if user is not None:
      auth.login(request, user)
      return redirect('home')
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
    if form.is_valid():
      form.save()
      return redirect(reverse('profile', args=[request.user.username]))
  else:
    form = ProfileForm(instance=request.user.profile)

  return render(request, 'update_profile.html', {'form': form})

def view_profile(request, username):
  profile = get_object_or_404(Profile, user__username=username)
  return render(request, 'view_profile.html', {'profile': profile})

def profile_management(request):
  if request.method == 'GET' and 'username' in request.GET:
    username = request.GET.get('username')
    return redirect('profile', username=username)
  return render(request, 'profile_management.html')

def home(request):
  return render(request, 'home.html')

@login_required
def create_post(request):
  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      post = form.save(commit=False)
      post.user = request.user
      post.save()
      return redirect('post_feed')
  else:
    form = PostForm()

  return render(request, 'create_post.html', {'form': form})

@login_required
def post_feed(request):
  # Get all the profiles that the user is following
  following_profiles = request.user.profile.following_set.all()
  # Get all the posts from the profiles the user is following
  posts = Post.objects.filter(user__profile__in=[follow.following for follow in following_profiles])
  return render(request, 'post_feed.html', {'posts': posts})