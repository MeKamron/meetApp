from django.urls import path
from .views import *

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name="register"),
]