# from django.conf import settings
# from django.conf.urls import static
from django.views.generic import TemplateView
from . import views
from django.urls import path

urlpatterns = [

    path('', views.crawl),

]

# This is required for static files while in development mode. (DEBUG=TRUE)
# No, not relevant to scrapy or crawling :)
# if settings.DEBUG:
#     urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

