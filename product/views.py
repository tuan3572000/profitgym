from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .models import ProductListingPage, ProductDetailPage


def product_listing(request):
    all_product_categories = ProductListingPage.objects.live().public().exact_type(ProductListingPage)
    all = [];
    category = {};
    category["all"] = [];
    category["bean"] = [];
    category["whey"] = [];
    context = {'categories':category}
    for product_category in all_product_categories:
        all.append({"title": product_category.title, "products": product_category.get_children().live().public().specific})

    category["all"] = all;
    category["bean"] = all;
    category["whey"] = all;
    return render(request, 'product/product_listing_page.html', context)