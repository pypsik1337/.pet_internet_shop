from django.urls import path

from main import views

# Имя приложения для того что бы в шаблонах можно было использовать main:index
app_name = 'main'

# Путь для каждой страницы
urlpatterns = [
    
    # Путь для главной страницы
    path('', views.index, name='index'),
    
    # Путь для страницы about
    path('about/', views.about, name='about'),
]