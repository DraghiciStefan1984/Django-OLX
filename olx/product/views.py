from django.shortcuts import render
from .models import Product, ProductImages

# Create your views here.
def product_list(request):
    product_list=Product.objects.all()
    return render(request, 'product/product_list.html', {'product_list':product_list})

def product_detail(request, product_slug):
    product_detail=Product.objects.get(slug=product_slug)
    product_images=ProductImages.objects.filter(product=product_detail)
    context={'product_detail':product_detail, 'product_images':product_images}
    return render(request, 'product/product_detail.html', context)