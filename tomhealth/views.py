from django.shortcuts import render
from .models import *

# Create your views here.
def index_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    

    return render(request, 'tomhealth/index.html',
        {'categories': categories,
         'products': products, 
        })


def product_view(request, id):
    categories = Category.objects.all()
    products = Product.objects.get(id=id)
    
    product_benefits = str(products.benefits.product_benefits)
    prod = product_benefits.split('.')
    print(product_benefits)
    print(prod)
    
    return render(request, 'tomhealth/product.html',
        {'products': products,
         'categories': categories,
         'product_benefits': product_benefits,
         'prod': prod})

def search_view(request, id):
    categories = Category.objects.all()
    products = Product.objects.all().filter(product_category=id)
    
    return render(request, 'tomhealth/index.html', 
        {'products': products,
         'categories': categories})
