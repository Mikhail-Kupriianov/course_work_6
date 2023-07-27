
from django.db import models
from django.utils.timezone import now

from users.models import User


class Message(models.Model):
    message_title = models.CharField(max_length=100, default='Новое сообщение', verbose_name='тема')
    message_content = models.TextField(verbose_name='содержимое', blank=True, null=True)
    message_created_at = models.DateTimeField(verbose_name='создано', default=now)
    message_owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, verbose_name='пользователь', blank=True, null=True)

    def __str__(self):
        return f'{self.message_title}\nСоздано: {self.message_created_at}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ('-message_created_at',)


if __name__ == '__main__':
    print('yes')
