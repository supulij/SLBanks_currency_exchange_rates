# Create your views here.

from django.shortcuts import render

from ExchangeRate.models import GetScrapy




def crawl(request):





    return render(request, 'ExchangeRate/Excha.html')
