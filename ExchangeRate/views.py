# Create your views here.

from django.shortcuts import render
from ExchangeRate.models import GetScrapy
from django.http import JsonResponse


def crawl(request):
    if request.method == 'POST':
        print("Its POST")
        return JsonResponse("Loading")

    if request.method == 'GET':
        context = GetScrapy.objects.all()

        return render(request, 'ExchangeRate/Excha.html', {'context': context})
