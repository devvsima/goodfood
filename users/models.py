from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=12, blank=True, null=True, verbose_name='Номер телефону')

    class Meta:
        db_table = "user"
        verbose_name = "користувач"
        verbose_name_plural = "Користувачі"

    def __str__(self) -> str:
        return self.username
