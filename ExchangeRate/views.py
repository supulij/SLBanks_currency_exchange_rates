# Create your views here.

from django.shortcuts import render

from ExchangeRate.models import GetScrapy


def crawl(request):

    context = GetScrapy.objects.all()

    return render(request, 'ExchangeRate/Excha.html', {'context':context})
