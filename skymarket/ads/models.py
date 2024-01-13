from django.conf import settings
from django.db import models


class Ad(models.Model):
    title = models.CharField('Название', max_length=200)
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание', blank=True)
    image = models.ImageField('Картинка', upload_to='ads', blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               verbose_name='Автор', related_name='ads')
    created_at = models.DateTimeField('Дата и время создания', auto_now_add=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        result = self.title[:40]
        if len(self.title) > 40:
            result += '...'
        return result


class Comment(models.Model):
    text = models.CharField('Название', max_length=1000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               verbose_name='Автор', related_name='comments')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE,
                           verbose_name='Объявление', related_name='comments')
    created_at = models.DateTimeField('Дата и время создания', auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        result = self.text[:40]
        if len(self.text) > 40:
            result += '...'
        return result

