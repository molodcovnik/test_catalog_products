from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название продукта')
    description = models.TextField(verbose_name='Описание продукта')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Цена продукта')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления продукта',)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.title}'
