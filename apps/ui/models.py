from django.db import models
from apps.product_info.models import Product


# Create your models here.
class GroceryItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)


class User(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    preferred_location = models.TextField()


class GroceryList(models.Model):
    items = models.ManyToManyField(GroceryItem)
    user = models.ForeignKey(User, on_delete=models.CASCADE)