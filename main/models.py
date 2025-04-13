from django.contrib.auth.models import User
from django.db import models


from rest_framework.pagination import PageNumberPagination

class FoodPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class Category(models.Model):
    name = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.name


class Foods(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Foods, on_delete=models.CASCADE)


from django.db import models

# Create your models here.
