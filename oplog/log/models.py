from django.db import models
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Watch(models.Model):
    watch = models.CharField(
        max_length=10
    )
    
    def __str__(self):
        return self.watch

class Duty(models.Model):
    duty = models.CharField(
        max_length=5
    )
    
    def __str__(self):
        return self.duty

class Record(models.Model):

    
    text = models.TextField(
        'Текст записи',
        help_text='Введите текст записи'
    )
    pub_date = models.DateTimeField(
        'Дата записи',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='record',
        verbose_name='Автор'
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return self.text[:15]


