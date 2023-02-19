from django.urls import path
from .views import services_view, services_direct_view

app_name = 'services'

urlpatterns = [
    path('<int:id>/<slug:slug>', services_direct_view, name='services_direct_view'),
    path('', services_view, name='services_view')
]