from django.urls import path
from Bryggelogg import views

# TEMPLATE TAGGING:
app_name = 'Bryggelogg'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('Bryggelogg/', views.bryggelogg_view, name='bryggelogg'),
    path('dashboard/', views.dashboard_view.as_view(), name='dashboard'),
]
