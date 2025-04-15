
from rest_framework import pagination
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Foods, Category, Comment
from .serializers import FoodsSerializer, CategorySerializer, CommentSerializer



class FoodsListView(ListAPIView):
    queryset = Foods.objects.all()
    serializer_class = FoodsSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]IsAuthenticated

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class CommentListView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
