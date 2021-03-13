""" apps/main/views.py """

from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    """ Home page. """
    return render(request, 'main/home.html')


def create(request, **kwargs):
    """ Create the image of the barcode. """
    code = kwargs['barcode']

    return JsonResponse({
        'status': 'ready'
    })
