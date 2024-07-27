from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('signup/', views.signup, name='signup'),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('profile/edit/', views.create_or_update_profile, name='edit_profile'),
  path('profile/<str>:username', views.view_profile, name='profile'),
]