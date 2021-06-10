from accounts.serializers import ProfileSerializer, UserSerializer
from django.db.models import fields
from rest_framework import generics
from rest_framework import serializers
from .models import Post, SubCategory, Category, Comment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = "__all__"

    def get_author(self, obj):
        return obj.author.username

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    video = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Post
        fields = ['author', 'image', 'video', 'title', 'category', 'sub_category', 'body', 'publish', 'comments']
    
    def get_image(self, obj):   
        try:
            image = obj.image.url
        except:
            image = None
        return image
    
    def get_video(self, obj):
        try:
            video = obj.video.url
        except:
            video = None
        return video

    def get_author(self, obj):
        return obj.author.username


class CategorySerializer(serializers.ModelSerializer):
    profiles = ProfileSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['title', 'profiles' ]

      
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

    