"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

# Импорт для использования debug режима
from app.settings import DEBUG, MEDIA_URL, MEDIA_ROOT


# Путь для каждой страницы сайта
urlpatterns = [
    
    # Стандартный путь, в админскую панель
    path("admin/", admin.site.urls),
    
    # Путь на главную страницу. include используется так как есть другой urlconfig в main
    path("", include("main.urls", namespace="main")),
    
    # Путь на страницу каталога. include используется так как есть другой urlconfig в goods
    path("catalog/", include("goods.urls", namespace="catalog")),
    
    # Путь на страницу пользователя. include используется так как есть другой urlconfig в users
    path("user/", include("users.urls", namespace="user")),
    
    
]

# Проверка, что debug режим включен 
if DEBUG:
    
    # Добавляется в список выше, путь для bebug_toolbar
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
    
    
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
