# Create your views here.

from django.shortcuts import render
from ExchangeRate.models import GetScrapy
from django.core.management import call_command
from ExchangeRate.forms import Homeform


def home(request):
    if request.method == 'POST':
        form = Homeform(request.POST)

        if form.is_valid():
            currency = form.cleaned_data['post']

        context = GetScrapy.objects.filter(currency_name=currency)
        last_updated = context[0].updated

        # form = Homeform()

        args = {'form': form, 'context': context, 'currency': currency, 'last_updated': last_updated}
        return render(request, 'ExchangeRate/Excha.html', args)

    if request.method == 'GET':
        form = Homeform()
        # call_command('crawl')

        return render(request, 'ExchangeRate/Home.html', {'form': form})







#
#
# def crawl(request):
#     if request.method == 'POST':
#         # call_command('crawl')
#         # return JsonResponse("Loading")
#         context = GetScrapy.objects.all()
#         return render(request, 'ExchangeRate/Excha.html', {'context': context})
#
#     if request.method == 'GET':
#         context = GetScrapy.objects.all()
#
#         return render(request, 'ExchangeRate/Excha.html', {'context': context})
