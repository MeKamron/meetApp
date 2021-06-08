from django.db.models import query
from django.contrib.auth.models import User
from django.urls.resolvers import RegexPattern
from rest_framework import generics, permissions, serializers
from .serializers import ProfileSerializer, StatusSerializer, RegionSerializer, UserSerializer
from .models import Profile, Status, Region
from .permissions import IsOwnerOrReadOnly


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class  = ProfileSerializer

    def post(self, request, *args, **kwargs):
            region = request.data.get('region')
            manzil = request.data.get('manzil')
            region = Region.objects.get(name=region)
            request.data['region'] = region.id
            request.data['manzil'] = manzil
            request.data['user'] = request.user.id

            return self.create(request, *args, **kwargs)

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class StatusList(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class  = StatusSerializer

class StatusDetail(generics.RetrieveAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class RegionList(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class RegionDetail(generics.RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


