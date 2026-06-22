from django.urls import path
from users import views


app_name = 'users'

# url для приложения users
urlpatterns = [
    
    # Авторизация пользователя
    path('login/', views.login, name='login'),
    
    # Регистрация пользователя
    path('registration/', views.registration, name='registration'),
    
    # Профил пользователя
    path('profile/', views.profile, name='profile'),
    
    # Выход из профиля
    path('logout/', views.logout, name='logout'),
]