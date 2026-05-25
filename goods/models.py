from django.db import models


# Классы для ORM, модель категорий
class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)


    # Класс для изменения наименования внутри админской панели
    class Meta:
        db_table = "category"
        
        
    def __str__(self):
        return self.name


# Классы для ORM, модель продукты
class Products(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="goods_images", blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE)


    # Класс для изменения наименования внутри админской панели
    class Meta:
        db_table = "product"


    def __str__(self):
        return self.name
    
    # Метод форматирует строку id к виду 00001
    def display_id(self):
        return f'{self.id:05}'
    
    def sell_price(self):
        if self.discount:
            return round(self.price - (self.price * self.discount) / 100, 2)
        
        return self.price