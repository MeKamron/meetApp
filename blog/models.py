from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=64, verbose_name="Kategoriya")
    slug = models.SlugField(max_length=64)

    def __str__(self) -> str:
        return self.title

class SubCategory(models.Model):
    title = models.CharField(max_length=64, verbose_name="Subkategoriya")
    parent_cateogory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    slug = models.SlugField(unique=True, max_length=64)
    
    def __str__(self) -> str:
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=256, unique_for_date='publish')
    photo = models.ImageField(upload_to='posts/photos/', blank=True, null=True)
    video = models.FileField(upload_to='posts/videos/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="posts", blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-publish',) 
    
    def __str__(self):
        return self.title