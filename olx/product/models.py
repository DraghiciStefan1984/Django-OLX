from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    CONDITION_TYPE=(('New', 'New'), ('Used', 'Used'))

    name=models.CharField(max_length=100)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    description=models.TextField(max_length=1000)
    condition=models.CharField(max_length=100, choices=CONDITION_TYPE)
    price=models.DecimalField(max_digits=15, decimal_places=5)
    created=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='products/', blank=True, null=True)

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'

    def __str__(self):
        return self.category_name