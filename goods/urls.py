from django.urls import path
from goods import views


app_name = 'goods'

# url для приложения goods
urlpatterns = [
    
    # Страница каталога
    path('', views.catalog, name='index'),
    
    # Страница продукта
    path('product/', views.product, name='product'),
]