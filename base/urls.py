from django.urls import path
from base.views import base_view, filter_view

app_name = 'index'

urlpatterns = [
    path('', base_view, name='base'),
    path('filters/', filter_view, name='filter'),
]
