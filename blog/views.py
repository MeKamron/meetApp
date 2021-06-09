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


# @api_view(['GET'])
# def postSearch(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         query = request.GET.get("query")
#         real_posts = []
#         for i in posts:
#             if query in i.title:
#                 real_posts.append(i)
#         serializers = PostSerializer(real_posts, many=True)
#         if len(real_posts) > 0:
#             return Response((serializers.data))
#         else:
#             return Response(("Not found"))


# @api_view(['GET'])
# def categorySearch(request):
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         query = request.GET.get("query")
#         real_categories = []
#         for i in categories:
#             if query in i.title or query in i.slug:
#                 real_categories.append(i)
#         serializers = CategorySerializer(real_categories, many=True)
#         if len(real_categories) > 0:
#             return Response((serializers.data))
#         else:
#             return Response(("Not found"))

# @api_view(['GET'])
# def subCategorySearch(request):
#     if request.method == 'GET':
#         subcategories = SubCategory.objects.all()
#         query = request.GET.get("query")
#         real_subcategories = []
#         for i in subcategories:
#             if query in i.title or query in i.slug:
#                 real_subcategories.append(i)
#         serializers = SubCategorySerializer(real_subcategories, many=True)
#         if len(real_subcategories) > 0:
#             return Response((serializers.data))
#         else:
#             return Response(("Not found"))
