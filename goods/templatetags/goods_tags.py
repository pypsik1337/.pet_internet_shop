from django import template
 
from goods.models import Categories

# Регистрация своего тега
register = template.Library()


@register.simple_tag()
def tag_categories():
    
    # Через метод objects получаем все значения из Categories 
     return Categories.objects.all()