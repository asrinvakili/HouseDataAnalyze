# from django.contrib.sites import requests
from django.contrib import messages
from django.shortcuts import render
from bs4 import BeautifulSoup

from base.forms import filter_form
from base.forms import filter_table
import re
import requests


# Create your views here.
def base_view(request):
    if request.method == 'POST':
        house = filter_table()
        for i in range(200):
            base_url = f'https://kilid.com/buy-apartment/tehran?page={i}'
            response = requests.get(base_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                divs = soup.find_all('div', class_='pb-4')
                for div in divs:
                    h = {}
                    p = div.select('div.pb-4 span.text-lg')
                    if len(p) != 0:
                        price = re.sub(r'قیمت:', r'', p[0].text)
                        house.price = price
                    else:
                        house.price = 'توافقی'
                    ad = div.select('p.inline-flex span')
                    location = ad[0].text
                    house.location = location
                    spans = div.select('div.-m-2 span.whitespace-nowrap')
                    for span in spans:
                        val = str(span.text).split()
                        if len(val) == 1:
                            noe = val[0]
                        elif val[1] == 'متر':
                            metr = val[0]
                            house.metr = metr
                        elif val[1] == 'خواب':
                            room = val[0]
                            house.rooms = room
                        elif val[1] == 'پارکینگ':
                            parking = val[0]
                            house.parking = parking
                    house.save()
        messages.add_message(request, messages.SUCCESS, 'Data loaded successfully')
        return render(request, 'index.html')
    else:
        messages.add_message(request, messages.ERROR, 'There was an error loading')
        return render(request, 'index.html')


def filter_view(request):
    if request.method == 'POST':
        form = filter_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = filter_form()
    return render(request, 'filter.html', {'form': form})
