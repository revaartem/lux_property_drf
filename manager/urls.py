from django.urls import path
from .views import manager_view, archived_applications, new_applications, application_to_archive, delete_application

app_name = 'manager'

urlpatterns = [
    path('', manager_view, name='manager_view'),
    path('new-applications/', new_applications, name='new_applications'),
    path('archived-applications/', archived_applications, name='archived_applications'),
    path('archived-applications/delete/<int:pk>', delete_application, name='delete_application'),
    path('new-applications/archive/<int:pk>', application_to_archive, name='application_to_archive')
]