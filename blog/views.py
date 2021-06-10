import re
from django.db.models import query
from rest_framework import generics, permissions
from .models import Category, Post, SubCategory, Comment
from accounts.models import Profile
from .serializers import PostSerializer, CategorySerializer, SubCategorySerializer, CommentSerializer
from .permissions import IsVerifiedOrReadOnly, IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication
from survey.permissions import IsSuperUserOrReadOnly
from rest_framework.decorators import api_view, authentication_classes, permission_classes
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

