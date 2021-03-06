from django.urls import path
from Bryggelogg import views

# TEMPLATE TAGGING:
app_name = 'Bryggelogg'

urlpatterns = [
    path('', views.index_view.as_view(), name='index'),
    path('Bryggelogg/', views.bryggelogg_view.as_view(), name='bryggelogg'),
    path('dashboard/', views.dashboard_view.as_view(), name='dashboard'),
    path('list/', views.bryggeloggListView.as_view(), name = ('list')),
    path('list/<int:pk>/', views.bryggeloggDetailView.as_view(), name = ('detail')),
    path('create_recipes/', views.RecipesCreateView.as_view(), name='recipes-create'),
    path('recipes_list/', views.RecipesListView.as_view(), name='recipes-list'),
    path('recipes_list/<int:pk>/', views.RecipesDetailView.as_view(), name='recipes-detail'),
    path('update/<int:pk>/', views.RecipesUpdateView.as_view(), name='recipes-update'),
    path('delete/<int:pk>/', views.RecipesDeleteView.as_view(), name='recipes-delete'),
]
