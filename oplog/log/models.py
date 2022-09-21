import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

from .utils import get_time


class Depart(models.Model):
    depart = models.CharField(max_length=10)
    
    
    class Meta:
        verbose_name = "Цех"
        verbose_name_plural = "Цеха"

    def __str__(self):
        return self.depart

class Position(models.Model):
    depart = models.ForeignKey(Depart, on_delete=models.CASCADE, null=True)
    position = models.CharField(max_length=10)
    
    
    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
    
    def __str__(self):
        return f'{self.position} {self.depart}'
    

class User(AbstractUser):
    bio = models.TextField(
        'Биография',
        blank=True,
    ) 
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='profile', default=1)


    class Meta:
        verbose_name = "Пользлователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f'{self.position} {self.first_name}'
    
    
class Watch(models.Model):
    watch = models.CharField(max_length=10)


    class Meta:
        verbose_name = "Вахта №"
        verbose_name_plural = "Вахты №"
        
    def __str__(self):
        return self.watch


class Duty(models.Model):
    duty = models.CharField(max_length=5)


    class Meta:
        verbose_name = "Смена с"
        verbose_name_plural = "Смены с"
        
        
    def __str__(self):
        return self.duty


class Record(models.Model):
    on_work = models.TextField(
        max_length=2000,
        blank=True,
        null=True,
    )
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE, related_name="record")
    duty_time = models.ForeignKey(Duty, on_delete=models.CASCADE, related_name="record")
    pub_date = models.DateField("Дата записи", default=datetime.date.today)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="record", verbose_name="Автор"
    )
    autodate = models.DateTimeField("Дата записи", auto_now_add=True)
    # position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='profile', default=1)
    workers = models.ManyToManyField(User, related_name='workers')
    

    class Meta:
        ordering = ["-autodate"]
        verbose_name = "Запись с шапкой"
        verbose_name_plural = "Записи с шапкой"

    def __str__(self):
        return f"{self.pub_date}"


class Text(models.Model):
    text = models.TextField(
        max_length=2000,
        blank=True,
        null=True,
    )
    pub_time = models.TimeField("Время записи", default=get_time)
    record = models.ForeignKey(
        Record,
        on_delete=models.CASCADE,
        related_name="texts",
        verbose_name="Записи смены",
    )

    class Meta:
        ordering = ["pub_time"]
        verbose_name = "Запись в смене"
        verbose_name_plural = "Записи в смене"
        
        
    def __str__(self):
        return f"{self.record} {self.pub_time} {self.text[:20]}"
