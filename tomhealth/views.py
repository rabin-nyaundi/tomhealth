from django.shortcuts import render
from .models import *

# Create your views here.
def index_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'tomhealth/index.html',
        {'categories': categories,
         'products': products})


def product_view(request, id):
    categories = Category.objects.all()
    products = Product.objects.get(id=id)
    return render(request, 'tomhealth/product.html',
        {'products': products,
         'categories': categories})

def search_view(request, id):
    categories = Category.objects.all()
    products = Product.objects.all().filter(product_category=id)
    
    return render(request, 'tomhealth/index.html', 
        {'products': products,
         'categories': categories})