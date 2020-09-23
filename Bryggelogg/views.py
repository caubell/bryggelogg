from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView,DetailView,FormView
from Bryggelogg.models import Bryggelogg
from Bryggelogg.forms import BryggeloggForm
from django.contrib.auth import get_user_model
from Bryggelogg.functions import avg_liter
import pandas as pd

# Login specific imports
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

user = get_user_model()

# Create your views here.
def index_view(request):
    return render(request, 'Bryggelogg/index.html', {})

def bryggelogg_view(request):
    form = BryggeloggForm()

    if request.method == 'POST':
        form = BryggeloggForm(request.POST)

        if form.is_valid():
            form.save()

    return render(request, 'Bryggelogg/bryggelogg.html', {'form': form})

class dashboard_view(TemplateView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        get_data = Bryggelogg.objects.all()

        # Calculating average sluttvolum
        liter_list = list(Bryggelogg.objects.all().values_list('sluttvolum', flat=True))
        for num in liter_list:
            if num == None:
                liter_list.remove(num)
        avg_liter = round(sum(liter_list)/len(liter_list),2)

        bryggevolum = [10, 12, 15, 12, 9]#get_data.sluttvolum
        labels = [1, 2, 3, 4, 5] #get_data.bryggenavn
        context = {
        'labels': labels,
        'data': bryggevolum,
        'avg_liter': avg_liter
        }
        return render(request, 'Bryggelogg/dashboard.html', context = context)

def chart_view(request):
    return render(request, 'Bryggelogg/chart.html', {})

def get_data(request, *args, **kwargs):
    data = {
    'sales': 100,
    'customers': 10,
    }
    return JsonResponse(data)

class ChartData(TemplateView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = user.objects.all().count()
        labels = ['Users', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
        default_items = [qs_count, 2, 3, 4, 5, 6]
        data = {
        'labels': labels,
        'default': default_items,
        }
        return Response(data)
