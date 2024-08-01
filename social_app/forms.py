from django import forms
from .models import Profile, Post, Comment

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['bio', 'profile_picture', 'birth_date', 'location']

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['content', 'media']

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['content']