"""lux_property URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from account.views import login_view, logout_view
from main_page.views import main_page_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_page.urls')),
    path('property/', include('property_single_page.urls')),
    path('property/menu/', include('properties_menu_page.urls')),
    path('about/', include('about_us.urls')),
    path('contact/', include('contact_us.urls')),
    path('services/', include('services.urls')),
    path('manager/', include('manager.urls')),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)