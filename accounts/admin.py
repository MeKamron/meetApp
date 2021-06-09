from accounts.views import FollowingList
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Region)
admin.site.register(Status)
admin.site.register(Profile)
admin.site.register(UserFollowing)