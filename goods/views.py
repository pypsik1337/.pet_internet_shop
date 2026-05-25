from django.shortcuts import render
from django.utils.text import slugify

from goods.models import Products


# Контроллер для отображения карточек с товарами на странице каталога, возвращает страницу goods.html и context
# В goods.html из словаря context переберается циклом значения и отоборажаются
def catalog(request):
    
    # Полечаем все данные из бд таблица Products
    goods = Products.objects.all()
    
    context = {
        "title": "Home - Каталог",
        "goods": goods
    }
    return render(request, "goods/catalog.html", context)

# Контроллер страницы товара
def product(request, product_slug):
    
    product = Products.objects.get(slug=product_slug)    
    
    context = {
        
        'product': product
    }
    
    return render(request, "goods/product.html", context=context)
