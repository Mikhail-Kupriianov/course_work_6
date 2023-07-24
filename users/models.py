from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта' )
    email_verify = models.BooleanField(default=False)

    phone = models.CharField(max_length=35, verbose_name='телефон', blank=False, null=False)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар',  blank=False, null=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
