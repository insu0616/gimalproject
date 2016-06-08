from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Shop, Review

# Create your views here.
def index(request):
    shop_list = Shop.objects.all()
    return render(request, 'blog/index.html', {'shop_list':shop_list})

def detail(request, pk):
    shop_detail = get_object_or_404(Shop, pk=pk)
    shop_detail.view += 1
    shop_detail.save()
    return render(request, 'blog/detail.html', {'shop_detail':shop_detail})
