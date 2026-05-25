from django.shortcuts import render

from goods.models import Categories

# Функция для отображения главной страницы
def index(request):
    

    
    # передаем в контекст. Для меню 
    context = {
        'title' : 'Home - Главная',
        'content' : 'Магазин мебели HOME',


    }
    return render(request, 'main/index.html', context)


# Функция для отображения страницы about
def about(request):
    context = {
        'title' : 'Home - О нас',
        'content' : 'Информация о магазине',
        'text_on_page': 'Магазин'

    }
    return render(request, 'main/about.html', context)
