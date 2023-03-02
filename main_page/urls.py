from django.urls import path
from .views import all_data

app_name = 'main_page'

urlpatterns = [
    path('', all_data, name='all_data')
]