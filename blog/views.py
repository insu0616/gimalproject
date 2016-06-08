from django.shortcuts import render
from .models import Category, Shop, Review

# Create your views here.
def index(request):
    shop_list = Shop.objects.all()
    return render(request, 'blog/index.html', {'shop_list':shop_list})
