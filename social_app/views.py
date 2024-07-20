from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout

def signup(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')

    if not (username and password and email):
      return JsonResponse({'error': 'Username, Password, Email are required'}, status=400)
