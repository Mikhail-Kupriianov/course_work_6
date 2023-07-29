from django.db import models

from users.models import User


class Client(models.Model):
    client_second_name = models.CharField(max_length=50, verbose_name='фамилия')
    client_first_name = models.CharField(max_length=50, verbose_name='имя')
    client_surname = models.CharField(max_length=50, blank=True, null=True, verbose_name='отчество')
    client_email = models.EmailField(verbose_name='почта')
    client_comments = models.TextField(verbose_name='комментарии', blank=True, null=True)
    client_owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, verbose_name='пользователь', blank=True, null=True)

    def __str__(self):
        return f'{self.client_second_name} {self.client_first_name} {self.client_email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ('client_second_name',)
