from django.shortcuts import (HttpResponse, render)
from post.models import Product, Category, Review
# from datetime import datetime


def main_view(request):
    if request.method == 'GET':
        # print(posts.category_related.all())
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        post = Product.objects.all()
        return render(request, 'products/products.html', context={'posts': post})


def category_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'products/categories.html', context={'categories': categories})


def products_detail_view(request, product_id):
    if request.method == 'GET':
        details = Product.objects.get(id=product_id)
        return render(request, 'products/detail.html', context={'details': details})


def product_review_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        return render(request, 'products/detail.html', context={'reviews': reviews})

        # return HttpResponse('Hello')
#
# def Date_view(request):
#     current_date = datetime.now()
#     format_date = current_date.strftime('%Y-%m-%d')
#     return HttpResponse(f'Current Date {format_date}')
#
# def Goodby_view(request):
#     return HttpResponse('Goodbye user!')



