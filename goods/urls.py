from django.urls import path
from goods import views


app_name = 'goods'

# url для приложения goods
urlpatterns = [
    
    # Страница каталога
    path('<slug:category_slug>/', views.catalog, name='index'),
    
    # Страница продукта
    path('product/<slug:product_slug>/', views.product, name='product'),
]