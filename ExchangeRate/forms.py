from django import forms
from ExchangeRate.models import GetScrapy


class Homeform(forms.Form):
    values = GetScrapy.objects.values_list('currency_name', flat=True).distinct()
    list = []

    for item in values:
        if item not in list:
            list.append(item)
        else:
            pass
    # print(list)

    post = forms.CharField(label='Select the currency', widget=forms.Select(choices=[(x,x) for x in list]))


    class Meta:
        model = GetScrapy
        fields = ['currency_name']