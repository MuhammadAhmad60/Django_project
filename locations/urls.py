from django.urls import path
from . import views  
urlpatterns = [
    path('', views.home, name='home'),
    path('get_provinces/', views.get_provinces, name='get_provinces'),
    path('get_cities/', views.get_cities, name='get_cities'),
    path('save_location/', views.save_location, name='save_location'),


     # CRUD views
    path('locations/', views.location_list, name='location_list'),
    path('locations/edit/<int:pk>/', views.edit_location, name='edit_location'),
    path('locations/delete/<int:pk>/', views.delete_location, name='delete_location'),
    path('delete_location/<int:pk>/', views.delete_location, name='delete_location_shortcut'), 
]
