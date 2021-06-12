from django.db import models
from django.contrib.auth.models import User
from blog.models import Category, SubCategory
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Region(models.Model):
    name = models.CharField(max_length=64, verbose_name="Viloyat nomi")

    def __str__(self) -> str:
        return self.name


class Status(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/photos/', blank=True,null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="users")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="users")
    manzil = models.CharField(max_length=300, blank=True)
    category = models.ManyToManyField(Category, related_name="profiles")
    sub_category = models.ManyToManyField(SubCategory, related_name="profiles", blank=True, null=True)
    bio = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return self.user.username



class UserFollowing(models.Model):
    user = models.ForeignKey(UserModel, related_name="following", on_delete=models.CASCADE)
    following_user = models.ForeignKey(UserModel, related_name="followers", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user','following_user'],  name="unique_followers")
        ]

        ordering = ["-created"]

    def __str__(self):
        return f"{self.user_id} follows {self.following_user_id}"

