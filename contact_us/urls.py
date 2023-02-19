from django.urls import path
from .views import contact_us_view, confirmation

app_name = 'contact_us'

urlpatterns = [
    path('', contact_us_view, name='contact_us_view'),
    path('confirmation/', confirmation, name='confirmation'),
]