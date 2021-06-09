from django.contrib.auth.models import User
from rest_framework import generics, permissions, serializers, viewsets
from .serializers import *
from .models import Profile, Status, Region, UserFollowing
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from slugify import slugify
from rest_framework import filters

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


# class UserFollowingViewSet(viewsets.ModelViewSet):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     serializer_class = UserFollowingSerializer
#     queryset = UserFollowing.objects.all()

class FollowingList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = UserFollowing
    serializer_class = FollowingSerializer


class FollowingDetail(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = UserFollowing
    serializer_class = FollowingSerializer


class FollowersView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = UserFollowing
    serializer_class = FollowersSerializer




# @api_view(['GET'])
# def userSearch(request):
#     if request.method == 'GET':
#         users = User.objects.all()
#         query = request.GET.get("query")
#         real_users = [] 
#         for i in users:
#             if query in i.username:
#                 real_users.append(i)
        
#         serializers = UserSerializer(real_users, many=True)
#         if len(real_users) > 0:
#             return Response((serializers.data))  
#         else:
#             return Response(("Not found"))
        