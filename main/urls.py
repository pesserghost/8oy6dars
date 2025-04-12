from django.urls import path
from .views import FoodsListView, CategoryListView, CommentListView

urlpatterns = [
    path('api/foods/', FoodsListView.as_view(), name='foods-list'),
    path('api/categories/', CategoryListView.as_view(), name='category-list'),
    path('api/comments/<int:food_id>/', CommentListView.as_view(), name='comment-list'),
]