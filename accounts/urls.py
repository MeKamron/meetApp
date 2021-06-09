from accounts.serializers import ProfileSerializer
from django.urls import path
from .views import *

urlpatterns = [
    path('profiles/', ProfileList.as_view()),
    path('profiles/<int:pk>/', ProfileDetail.as_view()),
    path('statuses/', StatusList.as_view()),
    path('statuses/<int:pk>/', StatusDetail.as_view()),
    path('regions/', RegionList.as_view()),
    path('regions/<int:pk>/', RegionDetail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    # path('users/search/', userSearch, name="user_search")
]