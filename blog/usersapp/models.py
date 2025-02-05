from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class BlogUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_author = models.BooleanField(default=False)

    # Переопределение метода save
    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        # СОздаем Profile
        # Если Profile не создан
        if not Profile.objects.filter(user=self).exists():
            Profile.objects.create(user=self)
        return user

class Profile(models.Model):
    # При создании пользователя создать Profile
    info = models.TextField(blank=True)
    user = models.OneToOneField(BlogUser, on_delete=models.CASCADE)

# @receiver(post_save, sender=BlogUser)
# def create_profile(sender, instance, created, **kwargs):
#     if created:  # ✅ Проверяем, создаётся ли новый объект
#         print('Сработал обработчик сигнала: создаём профиль')
#         Profile.objects.create(user=instance)