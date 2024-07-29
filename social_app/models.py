from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  bio = models.TextField(max_length=300, blank=True)
  profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
  birth_date = models.DateField(null=True, blank=True)
  location = models.CharField(max_length=100, blank=True)

class Post(models.Model):
  user = models.ForeignKey(Profile, on_delete=models.CASCADE)
  content = models.TextField(max_length=300)
  image = models.ImageField(upload_to='post_images/', blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Like(models.Model):
  user = models.ForeignKey(Profile, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
  user = models.ForeignKey(Profile, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  content = models.TextField(max_length=300)
  created_at = models.DateTimeField(auto_now_add=True)

class Follow(models.Model):
  follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='follower')
  following = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
  created_at = models.DateTimeField(auto_now_add=True)
  
class Unfollow(models.Model):
  follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='unfollower')
  following = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='unfollowing')
  unfollowed_at = models.DateTimeField(auto_now_add=True)