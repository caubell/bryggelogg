from django.urls import path
from Bryggelogg import views

# TEMPLATE TAGGING:
app_name = 'Bryggelogg'

urlpatterns = [
    path('', views.index_view.as_view(), name='index'),
    path('Bryggelogg/', views.bryggelogg_view.as_view(), name='bryggelogg'),
    path('dashboard/', views.dashboard_view.as_view(), name='dashboard'),
    path('list/<int:pk>/', views.bryggeloggDetailView.as_view(), name = ('detail')),
    path('list/', views.bryggeloggListView.as_view(), name = ('list')),
    path('create_recipes/', views.RecipesCreateView.as_view(), name='recipes-create'),
    path('recipes_list/', views.RecipesListView.as_view(), name='recipes-list'),  
    path('recipes_detail/<int:pk>/', views.RecipesDetailView.as_view(), name='recipes-detail'),
]
