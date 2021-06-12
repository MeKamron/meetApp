from accounts.serializers import ProfileSerializer, UserSerializer
import re
from django.db.models import query
from rest_framework import generics, permissions
from .models import Category, Post, SubCategory, Comment
from accounts.models import Profile, UserFollowing
from .serializers import PostSerializer, CategorySerializer, SubCategorySerializer, CommentSerializer
from .permissions import IsVerifiedOrReadOnly, IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication
from survey.permissions import IsSuperUserOrReadOnly
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import filters
from .paginations import CustomPagination
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

UserModel = get_user_model()



class PostList(generics.ListCreateAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    pagination_class = CustomPagination
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsVerifiedOrReadOnly]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        user_id = None
        if self.request and hasattr(self.request, "user"):
            user_id = self.request.user
        serializer.save(author=user_id)

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
            user_id = None
            if self.request and hasattr(self.request, "user"):
                user_id = self.request.user
            serializer.save(author=user_id)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]
    authentication_classes = [TokenAuthentication]


class CategoryList(generics.ListCreateAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperUserOrReadOnly]
    authentication_classes = [TokenAuthentication]


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperUserOrReadOnly]
    authentication_classes = [TokenAuthentication]


class SubCategoryList(generics.ListCreateAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperUserOrReadOnly]
    authentication_classes = [TokenAuthentication]


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    authentication_classes = [TokenAuthentication]
    


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def mixed_posts(request, user_id):
    if request.method == "GET":
        user = get_object_or_404(UserModel, id=user_id)
        followings = user.following.all()
        following_users = [following.following_user for following in followings]
        related_posts = Post.objects.filter(author__in=following_users)
        serializers = PostSerializer(related_posts, many=True)
        # mixed_posts = []
        # if related_posts:
        #     for post in related_posts:
        #         if post.id % 2 == 0 and post not in mixed_posts:
        #             mixed_posts.append(post)
        #     for post in related_posts:
        #         if post.id%2 != 0 and post not in mixed_posts:
        #             mixed_posts.append(post)
        #     serializers = PostSerializer(mixed_posts, many=True)
        return Response(serializers.data)
    

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def recommendations(request, user_id):
    if request.method == "GET":
        user = get_object_or_404(UserModel, id=user_id)
        serializers = None
        related_profiles = None
        if user:
            related_profiles = Profile.objects.filter(category__in=user.profile.category.all())
            tavsiyalar = []
            followings = []
            for u_following in user.following.all():
                followings.append(u_following.following_user)

            for profile in related_profiles:
                if profile.user not in followings and profile.user not in tavsiyalar and profile.user != user:
                    tavsiyalar.append(profile.user)
            serializers = UserSerializer(tavsiyalar, many=True)
        return Response(serializers.data)