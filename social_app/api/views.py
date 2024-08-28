from rest_framework import viewsets
from rest_framework import permissions
from ..serializers import ProfileSerializer, PostSerializer, CommentSerializer, LikeSerializer, FollowSerializer, UnfollowSerializer
from ..models import Profile, Post, Comment, Like, Follow, Unfollow

class ProfileViewSet(viewsets.ModelViewSet):
  queryset = Profile.objects.all()
  serializer_class = ProfileSerializer
  permission_classes = [permissions.IsAuthenticated]

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  permission_classes = [permissions.IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  permission_classes = [permissions.IsAuthenticated]

class LikeViewSet(viewsets.ModelViewSet):
  queryset = Like.objects.all()
  serializer_class = LikeSerializer
  permission_classes = [permissions.IsAuthenticated]

class FollowViewSet(viewsets.ModelViewSet):
  queryset = Follow.objects.all()
  serializer_class = FollowSerializer
  permission_classes = [permissions.IsAuthenticated]

class UnfollowViewSet(viewsets.ModelViewSet):
  queryset = Unfollow.objects.all()
  serializer_class = UnfollowSerializer
  permission_classes = [permissions.IsAuthenticated]