from django.shortcuts import render
import csv
from .models import Data
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView, DetailView
import warnings
warnings.filterwarnings('ignore')
import csv, io
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'


def correct_null(str, prv, index):
    if str == '':
        return prv[index]
    else:
        return str


def data_upload(request):
    first = True
    template = "data_upload.html"
    data = Data.objects.all()
    prompt = {
        'order': 'Order of the CSV should be name, email, address,    phone, profile',
        'profiles': data
    }
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('latin-1')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        if first:
            first = False
            prv = column
        _, created = Data.objects.update_or_create(
            timestamp=column[0],
            node=column[1],
            datetime = column[2],
            gps_lat = correct_null(column[3], prv, 3),
            gps_lng = correct_null(column[4], prv, 4),
            gps_alt = correct_null(column[5], prv, 5),
            pm1 = correct_null(column[6], prv, 6),
            pm10 = correct_null(column[7], prv, 7),
            pm2_5 = correct_null(column[8], prv, 8),
            airpressure = correct_null(column[9], prv, 9),
            temperature = correct_null(column[10], prv, 10),
            humidity = correct_null(column[11], prv, 11)
        )
    context = {}
    return render(request, template, context)