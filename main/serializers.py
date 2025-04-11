from rest_framework import serializers
from .models import Category, Foods, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
class FoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields = '__all__'
        depth = 1

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['name']