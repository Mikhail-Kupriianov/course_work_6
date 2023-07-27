import datetime

from django.db import models
from django.template.defaulttags import now


class Distribution(models.Model):
    class Rhythm(models.TextChoices):
        EVERY_DAY = 'Раз в день', 'Раз в день'
        EVERY_WEEK = 'Раз в неделю', 'Раз в неделю'
        EVERY_MONTH = 'Раз в месяц', 'Раз в месяц'

    class Status(models.TextChoices):
        CREATED = 'Создана', 'Создана'
        ACTIVATED = 'Активирована', 'Активирована'
        FINISHED = 'Завершена', 'Завершена'

    distribution_name = models.CharField(max_length=255,
                                         blank=False,
                                         null=False,
                                         default='Рассылка',
                                         verbose_name='Рассылка')

    # message = models.ForeignKey('Messages', on_delete=models.CASCADE, verbose_name='Письмо для рассылки', **NULLABLE)
    # client_name = models.ManyToManyField(Client, verbose_name='Имя клиентов')

    distribution_start = models.DateTimeField(default=now,
                                              verbose_name='Дата начала рассылки')

    distribution_end = models.DateTimeField(default=now,
                                            verbose_name='Дата окончания рассылки')

    distribution_is_active = models.BooleanField(default=True,
                                                 verbose_name='Активная')

    periodicity = models.CharField(
        max_length=25,
        choices=Rhythm.choices,
        default=Rhythm.EVERY_DAY,
        verbose_name='Периодичность рассылки'
    )
    status = models.CharField(
        max_length=25,
        choices=Status.choices,
        default=Status.CREATED,
        verbose_name='Статус рассылки'
    )

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

    def __str__(self):
        return f"{self.distribution_name}"


if __name__ == '__main__':
    default_name = 'Рассылка ' + str(datetime.datetime.now())
    print(default_name)
