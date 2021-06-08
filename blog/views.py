from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from .permissions import IsVerifiedOrReadOnly, IsOwnerOrReadOnly
# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsVerifiedOrReadOnly]

    def post(self, request, *args, **kwargs):
        request.data['author'] = request.user.id
        return self.create(request, *args, **kwargs)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]