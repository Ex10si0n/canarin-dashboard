from django.shortcuts import render
from django.http import Http404
import csv
from .models import Data
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView, DetailView, ListView
import warnings
warnings.filterwarnings('ignore')
import csv, io
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'home'
        return context

def simpleDatetime(datetime):
    # 2020-10-03 09:21:17+00:00
    date, time = str(datetime).split(' ')
    y, m, d = date.split('-')
    time, utc = time.split('+')
    return "%s-%s %s" % (m, d, time)




def home(request, node):

    sample = 100
    labels = []
    data = []
    data1 = []
    PM1 = []
    PM10 = []
    PM2_5 = []
    airPressure = []
    gps_lat = 0
    gps_alt = 0
    gps_lng = 0
    queryset = Data.objects.order_by('timestamp').filter(node=node)
    modu = len(queryset) // sample + 1
    cnt = 0
    for canarin_data in queryset:
        if cnt % modu == 0:
            labels.append(simpleDatetime(canarin_data.datetime))
            data.append(canarin_data.temperature)
            data1.append(canarin_data.humidity)
            PM1.append(canarin_data.pm1)
            PM10.append(canarin_data.pm10)
            PM2_5.append(canarin_data.pm2_5)
            airPressure.append(canarin_data.airpressure)
            gps_lat = canarin_data.gps_lat
            gps_alt = canarin_data.gps_alt
            gps_lng = canarin_data.gps_lng
        cnt += 1


    return render(request, 'index.html', {
        'labels': labels,
        'data': data,
        'data1': data1,
        'PM1': PM1,
        'PM10': PM10,
        'PM2_5': PM2_5,
        'AP': airPressure,
        'node': node,
        'section': 'home',
        'GPS_lng': gps_lng,
        'GPS_alt': gps_alt,
        'GPS_lat': gps_lat
    })


class RawDataView(ListView):
    template_name = 'raw_data.html'
    model = Data
    paginate_by = 30

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'raw_data'
        return context


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
        'order': 'Order of the CSV should be in the following format',
        'profiles': data,
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

    return render(request, template, {'section': 'data_upload'})