from rest_framework import serializers
from .models import Profile, Post, Comment, Like, Follow, Unfollow

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Like
    fields = '__all__'

class FollowSerializer(serializers.ModelSerializer):
  class Meta:
    model = Follow
    fields = '__all__'

class UnfollowSerializer(serializers.ModelSerializer):
  class Meta:
    model = Unfollow
    fields = '__all__'