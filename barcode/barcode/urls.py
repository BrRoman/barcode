""" barcode/urls.py """

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('barcode/', include('apps.main.urls')),
]
