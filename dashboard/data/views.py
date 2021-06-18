from django.shortcuts import render
import csv
from .models import Data
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView, DetailView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

def import_csv():
    f = open('../../data.csv', 'r')
    with f:
        reader = csv.reader(f)
        for row in reader:
            d = Data(
                timestamp=row[0],
                node=row[1],
                datetime=row[2],
                gps_lat=row[3],
                gps_lng=row[4],
                gps_alt=row[5],
                pm1=row[6],
                pm10=row[7],
                pm2_5=row[8],
                airpressure=row[9],
                temperature=row[10],
                humidity=row[11],
            )

        d.save()
