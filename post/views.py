from django.shortcuts import (HttpResponse, render, redirect)
from post.models import Product, Category, Review
from post.forms import ProductCreateForm, CategoryCreateForm, ReviewCreateForm, ProductCreateForm2
from django.conf import settings


# from datetime import datetime


def main_view(request):
    if request.method == 'GET':
        print(request.user)
        # print(posts.category_related.all())
        return render(request, 'layouts/index.html', {'title': 'Home'})


def products_view(request):
    if request.method == 'GET':
        post = Product.objects.all()

        search = request.GET.get('search')
        print(search)

        if search:
            post = post.filter(name__icontains=search)

        max_page = post.count() / settings.PAGE_SIZE

        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        page = int(request.GET.get('page', 1))
        start = (page - 1) * settings.PAGE_SIZE
        end = page * settings.PAGE_SIZE
        post = post[start:end]

        return render(request, 'products/products.html',
                      context={'posts': post, 'pages': range(1, max_page + 1), 'title': 'Product'})


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


def update_view(request, product_id):
    try:
        post = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'errors/404.html')
    if request.method == 'GET':
        form = ProductCreateForm2(instance=post)
        context = {'form': form}
        return render(request, 'products/update.html', context)
    if request.method == 'POST':
        form = ProductCreateForm2(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect(f'/posts/{product_id}/')
        # return HttpResponse('Hello')
        return render(request, 'products/detail.html', {'form': form})

# def Date_view(request):
#     current_date = datetime.now()
#     format_date = current_date.strftime('%Y-%m-%d')
#     return HttpResponse(f'Current Date {format_date}')
#
# def Goodby_view(request):
#     return HttpResponse('Goodbye user!')
