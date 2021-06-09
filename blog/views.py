import re
from rest_framework import generics, permissions
from .models import Category, Post, SubCategory, Comment
from accounts.models import Profile
from .serializers import PostSerializer, CategorySerializer, SubCategorySerializer, CommentSerializer
from .permissions import IsVerifiedOrReadOnly, IsOwnerOrReadOnly
from survey.permissions import IsSuperUserOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import filters
from .paginations import CustomPagination



class PostList(generics.ListCreateAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    pagination_class = CustomPagination
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsVerifiedOrReadOnly]

    def perform_create(self, serializer):
        user_id = None
        if self.request and hasattr(self.request, "user"):
            user_id = self.request.user
        serializer.save(author=user_id)

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsVerifiedOrReadOnly]

    def perform_create(self, serializer):
            user_id = None
            if self.request and hasattr(self.request, "user"):
                user_id = self.request.user
            serializer.save(author=user_id)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

class CategoryList(generics.ListCreateAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperUserOrReadOnly]


class SubCategoryList(generics.ListCreateAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperUserOrReadOnly]


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


@api_view(['GET'])
def related_post(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        profile_data = None
        profiles = [x for x in Profile.objects.all()]
        for profile in profiles:
            if profile.user.id == request.user.id:
                profile_data = profile

        real_posts = []
        for post in posts:
            if post.category in profile_data.category.all() or post.sub_category in profile_data.sub_category.all():
                real_posts.append(post)
        serializers = PostSerializer(real_posts, many=True)
        return Response(serializers.data)

