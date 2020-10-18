from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import CreateView, TemplateView, DetailView, FormView, ListView, View, UpdateView, DeleteView
from Bryggelogg.models import Bryggelogg, Recipes, Malt, Hop
from Bryggelogg.forms import BryggeloggForm, RecipesForm, MaltFormSet, HopFormSet
from django.contrib.auth import get_user_model
from Bryggelogg.functions import avg_liter
import pandas as pd

# For add/remove specific functionality in the formset
from django.db import transaction
from django.urls import reverse_lazy

# Login specific imports
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

user = get_user_model()


class RecipesCreateView(CreateView):
    model = Recipes
    form_class = RecipesForm
    success_url = reverse_lazy('Bryggelogg:recipes-list')

    def get_context_data(self, **kwargs):
        data = super(RecipesCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['malt'] = MaltFormSet(self.request.POST)
            data['hop'] = HopFormSet(self.request.POST)
        else:
            data['malt'] = MaltFormSet()
            data['hop'] = HopFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        malt = context['malt']
        hop = context['hop']
        with transaction.atomic():
            self.object = form.save()

            if malt.is_valid():
                malt.instance = self.object
                malt.save()

            if hop.is_valid():
                hop.instance = self.object
                hop.save()
        return super(RecipesCreateView, self).form_valid(form)

class RecipesListView(ListView):
    context_object_name = "recipes_list"
    model = Recipes

class RecipesDetailView(DetailView):
    context_object_name = 'recipes_detail'
    model = Recipes
    template_name = 'Bryggelogg/recipes_detail.html'

class RecipesUpdateView(UpdateView):
    model = Recipes
    form_class = RecipesForm
    template_name = 'Bryggelogg/recipes_form.html'

    def get_context_data(self, **kwargs):
        data = super(RecipesUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['malt'] = MaltFormSet(self.request.POST, instance=self.object)
            data['hop'] = HopFormSet(self.request.POST, instance=self.object)
        else:
            data['malt'] = MaltFormSet(instance=self.object)
            data['hop'] = HopFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        malt = context['malt']
        hop = context['hop']
        with transaction.atomic():
            self.object = form.save()
            if malt.is_valid():
                malt.instance = self.object
                malt.save()

            if hop.is_valid():
                hop.instance = self.object
                hop.save()
        return super(RecipesUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('Bryggelogg:recipes-detail', kwargs={'pk': self.object.pk})

class RecipesDeleteView(DeleteView):
    model = Recipes
    template_name = 'Bryggelogg/recipes_confirm_delete.html'
    success_url = reverse_lazy('Bryggelogg:recipes-list')

class index_view(TemplateView):
    template_name = 'Bryggelogg/index.html'

class bryggelogg_view(CreateView):
    form_class = BryggeloggForm
    model = Bryggelogg

class bryggeloggListView(ListView):
    context_object_name = "bryggelogg_list"
    model = Bryggelogg

class bryggeloggDetailView(DetailView):
    context_object_name = "bryggelogg_detail"
    model = Bryggelogg
    template_name = 'Bryggelogg/bryggelogg_detail.html'

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

class chart_view(View):
    def get(self,request):
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
