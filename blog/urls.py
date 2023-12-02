
from django.contrib import admin
from django.urls import path
from post import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
    path('', include('users.urls'))
    # path('', views.main_view),
    # path('products/', views.products_view),
    # path('categories/', views.category_view),
    # path('posts/create/', views.create_view),
    # path('posts/category/', views.create_categort_view),
    # path('posts/<int:product_id>/', views.products_detail_view)
    # path('hello/', views.Hello_view),
    # path('current_date/',views.Date_view),
    # path('goodby/',views.Goodby_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
