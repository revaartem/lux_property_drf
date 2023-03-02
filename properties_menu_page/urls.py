from django.urls import path
from .views import property_menu_data

app_name = 'properties_menu_page'

urlpatterns = [
    path('', property_menu_data, name='menu_page')
]