# Create your views here.


from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from scrapyd_api import ScrapydAPI

from uuid import uuid4
from ExchangeRate.models import GetScrapy
# from django.views.decorators.csrf import csrf_exempt

scrapyd = ScrapydAPI('http://localhost:6800')


# @csrf_exempt
@require_http_methods(['POST', 'GET'])
def crawl(request):
    if request.method == 'POST':
        unique_id = str(uuid4())

        settings = {
            'unique_id': unique_id,  # unique ID for each record for DB
        }

        scrapyd.schedule('default', 'Sampath', settings=settings)

        item = GetScrapy.objects.get(unique_id=unique_id)
        return render(request, 'ExchangeRate/Excha.html', {'data': item.to_dict['data']})

