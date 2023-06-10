from django.contrib.auth.models import AbstractUser
from django.db import models
from hasta_la_vista_money.constants import NumericParameter


class User(AbstractUser):
    def __str__(self):
        return self.username


class TelegramUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(
        max_length=NumericParameter.TWO_HUNDRED_FIFTY.value,
    )
    telegram_id = models.BigIntegerField(unique=True)