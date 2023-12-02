from django.shortcuts import (HttpResponse, render, redirect)
from post.models import Product, Category, Review
from post.forms import ProductCreateForm, CategoryCreateForm, ReviewCreateForm


# from datetime import datetime


def main_view(request):
    if request.method == 'GET':
        print(request.user)
        # print(posts.category_related.all())
        return render(request, 'layouts/index.html', {'title': 'Home'})


def products_view(request):
    if request.method == 'GET':
        post = Product.objects.all()
        return render(request, 'products/products.html', context={'posts': post, 'title': 'Product'})


def category_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'products/categories.html', context={'categories': categories, 'title': 'Category'})


def products_detail_view(request, product_id):
    if request.method == 'GET':
        form = ReviewCreateForm(request.POST)
        details = Product.objects.get(id=product_id)
        reviews = Review.objects.filter(product=product_id)
        data = {
            'reviews': reviews,
            'details': details,
            'form': form
        }
        return render(request, 'products/detail.html', context=data)
    elif request.method == 'POST':
        form = ReviewCreateForm(request.POST)
        if form.is_valid():
            Review.objects.create(**form.cleaned_data)
            context = {'form': form}
            return redirect(f'/posts/{product_id}')

        return render(request, 'products/detail.html', context=context)


# def product_review_view(request):
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         print(reviews)
#         return render(request, 'products/detail.html', context={'reviews': reviews})


def create_view(request):
    if request.method == 'GET':
        form = ProductCreateForm()
        return render(request, 'products/create.html', context={'form': form})
    if request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            return redirect('/products/')

        context = {'form': form}

        return render(request, 'products/create.html', context)


def create_categort_view(request):
    if request.method == 'GET':
        form = CategoryCreateForm()
        return render(request, 'products/category_create.html', context={'form': form})
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect('/categories/')

        context = {'form': form}

        return render(request, 'products/category_create.html', context)


def review_products(request):
    if request.method == 'GET':
        form = ReviewCreateForm()
        return render(request, 'products/detail.html', {'form': form})
    if request.method == 'POST':
        form = ReviewCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Review.objects.create(**form.cleaned_data)
            return redirect('/posts/{{ post.id }}/')

        context = {'form': form}

        return render(request, 'products/detail.html', context)


    # return HttpResponse('Hello')
#
# def Date_view(request):
#     current_date = datetime.now()
#     format_date = current_date.strftime('%Y-%m-%d')
#     return HttpResponse(f'Current Date {format_date}')
#
# def Goodby_view(request):
#     return HttpResponse('Goodbye user!')
