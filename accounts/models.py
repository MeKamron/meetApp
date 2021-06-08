from django.db import models
from django.contrib.auth.models import User
from blog.models import Category, SubCategory


class Region(models.Model):
    name = models.CharField(max_length=64, verbose_name="Viloyat nomi")

    def __str__(self) -> str:
        return self.name


class Status(models.Model):
    title = models.CharField(max_length=64)
    keyword = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/photos/', blank=True,null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="users")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="users")
    manzil = models.CharField(max_length=300, blank=True)
    category = models.ManyToManyField(Category, related_name="users")
    sub_category = models.ManyToManyField(SubCategory, related_name="users")
    bio = models.CharField(max_length=512)

    def __str__(self):
        return self.user.username
