
from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render

from goods.models import Products


# Контроллер для отображения карточек с товарами на странице каталога, возвращает страницу goods.html и context
# В goods.html из словаря context переберается циклом значения и отоборажаются
def catalog(request, category_slug):
    
    page = request.GET.get('page', 1)
    
    # Получаем все данные из бд таблица Products, если у нас все категории
    if category_slug == 'vse-tovary':
        goods = Products.objects.all()
    else:
    
        # Получаем все товары по fk category который из category_slug(kyhnya все их кухни)
        goods = get_list_or_404(Products.objects.filter(category__slug = category_slug))
    
    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))
    
    context = {
        "title": "Home - Каталог",
        "goods": current_page,
        'slug_url': category_slug
    }
    return render(request, "goods/catalog.html", context)

# Контроллер страницы товара
def product(request, product_slug):
    
    product = Products.objects.get(slug=product_slug)    
    
    context = {
        
        'product': product
    }
    
    return render(request, "goods/product.html", context=context)
