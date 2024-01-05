from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Ad(models.Model):
    image = models.ImageField(upload_to='ads/', verbose_name='Фото', **NULLABLE)
    title = models.CharField(max_length=255, verbose_name='Наименование товара', **NULLABLE)
    price = models.DecimalField(max_digits=8, decimal_places=0, verbose_name='Цена товара', **NULLABLE)
    description = models.TextField(**NULLABLE, verbose_name='Описание товара')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                               verbose_name='Владелец объявления', related_name='user')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Comment(models.Model):
    text = models.TextField(**NULLABLE, verbose_name='Текст коментария')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                               verbose_name='Автор коментария')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, **NULLABLE,
                           related_name='ad', verbose_name='Объявление')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания', **NULLABLE)

    def __str__(self):
        return f'{self.ad}'

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
