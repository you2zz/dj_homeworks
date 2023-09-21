import csv
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    with open(BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        list_stations = []
        for row in reader:
            list_stations.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(list_stations,10)
    page = paginator.get_page(page_number)
    data = page.object_list
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    context = {
        'bus_stations': data,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
