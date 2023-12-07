from post import views
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view),
    path('products/', views.products_view),
    path('categories/', views.category_view),
    path('posts/create/', views.create_view),
    path('posts/category/', views.create_categort_view),
    path('posts/<int:product_id>/', views.products_detail_view),
    path('posts/<int:product_id>/update/', views.update_view),
    # path('hello/', views.Hello_view),
    # path('current_date/',views.Date_view),
    # path('goodby/',views.Goodby_view),
]

