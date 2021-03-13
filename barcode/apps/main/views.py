""" apps/main/views.py """

import os

from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    """ Home page. """
    return render(request, 'main/home.html')


def create(request, **kwargs):
    """ Create the image of the barcode. """
    code = kwargs['barcode']

    os.system(
        "rm static/img/barcode/*.png; \
        barcode -b {0} -e 'ean13' -u mm -g 100x50 -S -o static/img/barcode/barcode.svg; \
        convert static/img/barcode/barcode.svg -transparent '#FFFFFF' -trim static/img/barcode/{0}.png; \
        rm static/img/barcode/*.svg"
        .format(code))

    return JsonResponse({
        'status': 'ready'
    })
