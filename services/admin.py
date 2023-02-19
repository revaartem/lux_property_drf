from django.contrib import admin
from .models import ServicesInfoOffer

# Register your models here.


@admin.register(ServicesInfoOffer)
class ServicesInfoOfferAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('header',), }
    list_display = ['header', 'small_description']
