from django.urls import path

from main.views import index

from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
]