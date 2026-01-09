from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_moderator = models.BooleanField(default=False, verbose_name="Модератор")
    is_student = models.BooleanField(default=True, verbose_name="Студент")
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return self.username