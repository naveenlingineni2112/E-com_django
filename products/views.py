from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, * args, **kwargs):
    return render(request,"index.html",{})

def product_view(request, * args, **kwargs):
    return render(request,"product.html",{})

def category_view(request, * args, **kwargs):
    return render(request,"category.html",{})
