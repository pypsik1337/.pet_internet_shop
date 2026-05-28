

from django import template
from django.http.request import urlencode

 
from goods.models import Categories

# Регистрация своего тега
register = template.Library()


@register.simple_tag()
def tag_categories():
    
    # Через метод objects получаем все значения из Categories 
     return Categories.objects.all()
 
 
@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
