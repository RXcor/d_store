from django.db import models
from django.db.models import Sum


class Role(models.Model):
    title = models.CharField(verbose_name="Наименование", max_length=15, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"

class Product(models.Model):
    vendor_code = models.CharField(verbose_name="Артикул", max_length=30, blank=False, unique=True)
    title = models.CharField(verbose_name="Наименование", max_length=30, blank=True)
    purchase_price = models.DecimalField(verbose_name="Цена закупки", max_digits=10, decimal_places=2)
    retail_price = models.DecimalField(verbose_name="Розничная цена", max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title + "({})".format(self.vendor_code)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

class Position(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField(verbose_name="Количество", null=False)
    #amount = models.DecimalField(verbose_name="Розничная цена", max_digits=10, decimal_places=2)
    basket = models.ForeignKey('Basket', on_delete=models.CASCADE)

    @property
    def amount(self):
        return self.number * self.product.retail_price

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = "Позиция"
        verbose_name_plural = "Позиции"

class Basket(models.Model):
    customer = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    @property
    def positions(self):
        return Position.objects.filter(basket=self)

    @property
    def amount(self):
        return Position.objects.filter(basket=self).aggregate(Sum('amount'))

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"
