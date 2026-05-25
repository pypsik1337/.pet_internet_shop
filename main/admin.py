from django.contrib import admin

from goods import models


# admin.site.register(models.Categories)
# admin.site.register(models.Products)


# Декоратор модели Categories, нужен для того что бы поле slug в админской панели автоматически заполнялось
@admin.register(models.Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    
    
# Декоратор модели Categories, нужен для того что бы поле slug в админской панели автоматически заполнялось  
@admin.register(models.Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}