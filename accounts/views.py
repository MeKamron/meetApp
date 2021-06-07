from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status



# def userCreate(request):
#     if request.POST:
#         # phone = request.POST.get("phone")
#         # username = request.POST.get("username")
#         # password = request.POST.get("password")
#         # get_user_model.create_user(phone=phone, username=username, password=password)
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return Response(status=200)
#     else:
#         form = UserCreationForm()
#         return Response(status=200)
            

class CustomUserCreate(APIView):
    permission_classes = [AllowAny]
    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)