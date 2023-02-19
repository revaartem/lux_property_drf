from django.urls import path
from .views import property_menu_view

app_name = 'properties_menu_page'

urlpatterns = [
    path('', property_menu_view, name='menu_page')
]