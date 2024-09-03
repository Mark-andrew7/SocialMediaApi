from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from ..serializers import UserSerializer, ProfileSerializer, PostSerializer, CommentSerializer, LikeSerializer, FollowSerializer, UnfollowSerializer, RegisterSerializer
from ..models import Profile, Post, Comment, Like, Follow, Unfollow
from django.contrib.auth.models import User
from rest_framework.views import APIView


class RegistrationView(APIView):
  serializer_class = RegisterSerializer
  permission_classes = [AllowAny]
  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [permissions.IsAuthenticated]
  http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class ProfileViewSet(viewsets.ModelViewSet):
  queryset = Profile.objects.all()
  serializer_class = ProfileSerializer
  permission_classes = [permissions.IsAuthenticated]
  http_method_names = ['get', 'post', 'put', 'patch', 'delete']

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