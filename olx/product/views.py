from django.shortcuts import render, get_object_or_404
from .models import Product, ProductImages, Category
from django.core.paginator import Paginator
from django.db.models import Count, Q


# Create your views here.
def product_list(request, category_slug=None):
    category=None
    product_list=Product.objects.all()
    category_list=Category.objects.annotate(total_products=Count('product'))
    if category_slug:
        category=get_object_or_404(Category, slug=category_slug)
        product_list=product_list.filter(category=category)
    search_query=request.GET.get('q')
    if search_query:
        product_list=product_list.filter(Q(name__icontains=search_query)|
                                        Q(description__icontains=search_query)|
                                        Q(condition__icontains=search_query)|
                                        Q(brand__brand_name__icontains=search_query)|
                                        Q(category__category_name__icontains=search_query))
    paginator = Paginator(product_list, 1)
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)
    context={'product_list':product_list, 'category_list':category_list, 'category':category} 
    return render(request, 'product/product_list.html', context)

def product_detail(request, product_slug):
    product_detail=get_object_or_404(Product, slug=product_slug)
    product_images=ProductImages.objects.filter(product=product_detail)
    context={'product_detail':product_detail, 'product_images':product_images}
    return render(request, 'product/product_detail.html', context)