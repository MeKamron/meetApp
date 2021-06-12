from django.contrib.auth.models import User
from rest_framework import generics, permissions, filters, status
from .serializers import *
from .models import Profile, Status, Region, UserFollowing
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

# class Logout(generics.APIView):
#     def get(self, request, format=None):
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)

class UserList(generics.ListAPIView):
    search_fields = ['username', 'first_name', 'last_name']
    filter_backends = (filters.SearchFilter,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class  = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
            region = request.data.get('region')
            manzil = request.data.get('manzil')
            region = Region.objects.get(name=region)
            request.data['region'] = region.id
            request.data['manzil'] = manzil
            request.data['user'] = request.user.id

            return self.create(request, *args, **kwargs)

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = [TokenAuthentication]


class StatusList(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class  = StatusSerializer
    authentication_classes = [TokenAuthentication]

class StatusDetail(generics.RetrieveAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    authentication_classes = [TokenAuthentication]

class RegionList(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    authentication_classes = [TokenAuthentication]

class RegionDetail(generics.RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    authentication_classes = [TokenAuthentication]


# class UserFollowingViewSet(viewsets.ModelViewSet):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     serializer_class = UserFollowingSerializer
#     queryset = UserFollowing.objects.all()

class FollowingList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = UserFollowing.objects.all()
    serializer_class = FollowingSerializer
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        user = None
        if self.request and hasattr(self.request, "user"):
            user = self.request.user
        serializer.save(user=user)


class FollowingDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = UserFollowing.objects.all()
    serializer_class = FollowingSerializer
    authentication_classes = [TokenAuthentication]


class FollowersView(generics.ListAPIView):
    queryset = UserFollowing.objects.all()
    serializer_class = FollowersSerializer
    authentication_classes = [TokenAuthentication]

