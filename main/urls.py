from django.urls import path

from main.apps import MainConfig
from main.views import DistributionListView, DistributionDetailView, DistributionCreateView, DistributionUpdateView, \
    DistributionDeleteView, index

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('distribution/', DistributionListView.as_view(), name='distributions'),
    path('distribution_item/<int:pk>', DistributionDetailView.as_view(), name='distribution_item'),
    path('distribution/create', DistributionCreateView.as_view(), name='distribution_create'),
    path('distribution/update/<int:pk>', DistributionUpdateView.as_view(), name='distribution_update'),
    path('distribution/delete/<int:pk>', DistributionDeleteView.as_view(), name='distribution_delete'),
]