from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('signup/', views.signup, name='signup'),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('profile/edit/', views.create_or_update_profile, name='edit_profile'),
  path('profile/<str:username>/', views.view_profile, name='profile'),
  path('profile_management/', views.profile_management, name='profile_management'),
  path('home/', views.home, name='home'),
  path('post/create/', views.create_post, name='create_post'),
  path('post/feed/', views.post_feed, name='post_feed'),
  path('like/<int:post_id>/', views.like_post, name='like_post'),
  path('comment/', views.add_comment, name='add_comment'),
  path('user/<str:username>/posts/', views.user_posts, name='user_posts'),
  path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
  path('my_posts/', views.my_posts, name='my_posts'),
]