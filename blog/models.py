import datetime

from django.db import models


class Blog(models.Model):
    blog_title = models.CharField(max_length=100, verbose_name='заголовок')
    blog_content = models.TextField(verbose_name='содержимое', blank=True, null=True)
    blog_preview = models.ImageField(upload_to='blog/', verbose_name='изображение', blank=True, null=True)
    blog_created_at = models.DateField(verbose_name='создан', default=datetime.date.today)
    blog_is_publicated = models.BooleanField(verbose_name='опубликован', default=False)
    blog_views_count = models.BigIntegerField(verbose_name='количество просмотров', default=0)

    def inc_view_count(self):
        self.blog_views_count += 1
        return self.blog_views_count

    def __str__(self):
        return f'{self.blog_title}\nСоздан: {self.blog_created_at}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ('blog_title',)
