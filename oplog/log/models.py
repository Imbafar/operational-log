import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    depart = models.CharField(max_length=30, blank=True)
    position = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"{self.depart} {self.position}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


def get_time():
    now = datetime.datetime.now()
    return now.time()


class Watch(models.Model):
    watch = models.CharField(max_length=10)

    def __str__(self):
        return self.watch


class Duty(models.Model):
    duty = models.CharField(max_length=5)

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

    class Meta:
        ordering = ["-autodate"]
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return f"{self.pub_date}"


class Text(models.Model):
    text = models.TextField(
        max_length=2000,
        blank=True,
        null=True,
    )
    pub_time = models.TimeField("Дата записи", default=get_time)
    record = models.ForeignKey(
        Record,
        on_delete=models.CASCADE,
        related_name="texts",
        verbose_name="Записи смены",
    )

    class Meta:
        ordering = ["pub_time"]

    def __str__(self):
        return f"{self.record} {self.pub_time} {self.text[:20]}"
