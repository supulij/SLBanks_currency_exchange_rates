# Create your views here.

from django.shortcuts import render
from ExchangeRate.models import GetScrapy
from django.core.management import call_command
from ExchangeRate.forms import Homeform
from django.utils.timezone import utc
from datetime import datetime


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

        now = datetime.now()
        previous = GetScrapy.objects.all()[0].updated.replace(tzinfo=None)
        timediffe = now - previous
        timed = timediffe.total_seconds()
        print(timed)

        # if timed > 50000:
        #     print(timed)
        #     print("call command to update database")
        #     call_command('crawl')
        #     print("finish updating")

        return render(request, 'ExchangeRate/Home.html', {'form': form})





