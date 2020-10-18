from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .models import ProductListingPage, ProductDetailPage


def product_listing(request):
    all_product_categories = ProductListingPage.objects.live().public().exact_type(ProductListingPage)
    context = {'categories':[]}
    for product_category in all_product_categories:
        context["categories"].append({"title": product_category.title, "products": product_category.get_children().live().public().specific})

    return render(request, 'product/product_listing_page.html', context)