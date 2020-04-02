from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class Product(models.Model):
    CONDITION_TYPE=(('New', 'New'), ('Used', 'Used'))

    name=models.CharField(max_length=100)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    brand=models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    description=models.TextField(max_length=1000)
    condition=models.CharField(max_length=100, choices=CONDITION_TYPE)
    price=models.DecimalField(max_digits=15, decimal_places=5)
    image=models.ImageField(upload_to='main_product/', blank=True, null=True)
    created=models.DateTimeField(default=timezone.now)
    slug=models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug=slugify(self.name)
            super().save(*args, **kwargs)


class Category(models.Model):
    category_name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='products/', blank=True, null=True)
    slug=models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        if not self.slug and self.category_name:
            self.slug=slugify(self.category_name)
            super().save(*args, **kwargs)


class Brand(models.Model):
    brand_name=models.CharField(max_length=50)

    class Meta:
        verbose_name='Brand'
        verbose_name_plural='Brands'

    def __str__(self):
        return self.brand_name


class ProductImages(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.product.name