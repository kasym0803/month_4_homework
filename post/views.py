from django.shortcuts import (HttpResponse, render)
from post.models import Product
# from datetime import datetime


def main_view(request):
    if request.method == 'GET':
        # posts = Product.objects.all()
        # print(posts)
        return render(request, 'layouts/index.html')

def products_view(request):
    if request.method == 'GET':
        post = Product.objects.all()
        return render(request, 'products/products.html', context={'posts': post})

        # return HttpResponse('Hello')
#
# def Date_view(request):
#     current_date = datetime.now()
#     format_date = current_date.strftime('%Y-%m-%d')
#     return HttpResponse(f'Current Date {format_date}')
#
# def Goodby_view(request):
#     return HttpResponse('Goodbye user!')



