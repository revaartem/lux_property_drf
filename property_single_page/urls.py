from django.urls import path
from .views import single_page_view

app_name = 'property_single_page'

urlpatterns = [
    path('<int:id>/<slug:slug>', single_page_view, name='single_page_view')
]