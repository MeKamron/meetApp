from django.db.models import fields
from rest_framework import generics
from rest_framework import serializers
from .models import Post, SubCategory, Category

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_author(self, obj):
      return obj.author.username

    class Meta:
        model = Post
        # exclude = ('author',)
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

      
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'