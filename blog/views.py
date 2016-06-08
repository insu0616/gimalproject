from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Shop, Review
from .forms import CategoryForm, ShopForm, ReviewForm
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    category_list = Category.objects.all()
    return render(request, 'blog/index.html', {'category_list':category_list})

def category_detail(request, pk):
    category_detail = get_object_or_404(Category, pk=pk)
    return render(request, 'blog/category_detail.html', {'category_detail':category_detail})

def shop_detail(request, pk):
    shop_detail = get_object_or_404(Shop, pk=pk)
    shop_detail.view += 1
    shop_detail.save()
    return render(request, 'blog/shop_detail.html', {'shop_detail':shop_detail})


def category_new(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '새로운 카테고리가 생성됐습니다.')
            return redirect(reverse('blog:index'))
    else:
        form = CategoryForm()
    return render(request, 'blog/category_form.html', {'form': form})


def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, '카테고리가 수정됐습니다.')
            return redirect(reverse('blog:index'))
    else:
        form = CategoryForm(instance=category)
    return render(request, 'blog/category_form.html', {'form': form})


def shop_new(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.category = category
            shop.save()
            messages.success(request, '가게가 생성됐습니다.')
            return redirect(reverse('blog:shop_detail', args=[shop.pk]))
    else:
        form = ShopForm()
    return render(request, 'blog/shop_form.html', {'form': form})

def shop_edit(request, category_pk, shop_pk):
    shop = get_object_or_404(Shop, pk=shop_pk)
    category = get_object_or_404(Category, pk=category_pk)
    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.category = category
            shop.save()
            messages.success(request, '가게가 수정됐습니다.')
            return redirect(reverse('blog:shop_detail', args=[shop.pk]))
    else:
        form = ShopForm(instance=shop)
    return render(request, 'blog/shop_form.html', {'form': form})
