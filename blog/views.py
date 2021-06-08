from rest_framework import generics, permissions
from .models import Category, Post, SubCategory
from accounts.models import Profile
from .serializers import PostSerializer, CategorySerializer, SubCategorySerializer
from .permissions import IsVerifiedOrReadOnly, IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsVerifiedOrReadOnly]

    def post(self, request, *args, **kwargs):
        request.data['author'] = request.user.id
        return self.create(request, *args, **kwargs)


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class SubCategoryList(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


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


@api_view(['GET'])
def postSearch(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        query = request.GET.get("query")
        real_posts = []
        for i in posts:
            if query in i.title:
                real_posts.append(i)
        serializers = PostSerializer(real_posts, many=True)
        if len(real_posts) > 0:
            return Response((serializers.data))
        else:
            return Response(("Not found"))


@api_view(['GET'])
def categorySearch(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        query = request.GET.get("query")
        real_categories = []
        for i in categories:
            if query in i.title or query in i.slug:
                real_categories.append(i)
        serializers = CategorySerializer(real_categories, many=True)
        if len(real_categories) > 0:
            return Response((serializers.data))
        else:
            return Response(("Not found"))

@api_view(['GET'])
def subCategorySearch(request):
    if request.method == 'GET':
        subcategories = SubCategory.objects.all()
        query = request.GET.get("query")
        real_subcategories = []
        for i in subcategories:
            if query in i.title or query in i.slug:
                real_subcategories.append(i)
        serializers = SubCategorySerializer(real_subcategories, many=True)
        if len(real_subcategories) > 0:
            return Response((serializers.data))
        else:
            return Response(("Not found"))
