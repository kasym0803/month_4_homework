
from django.contrib import admin
from django.urls import path
from post import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view),
    path('products/', views.products_view),
    path('categories/', views.category_view)
    # path('hello/', views.Hello_view),
    # path('current_date/',views.Date_view),
    # path('goodby/',views.Goodby_view),
]
