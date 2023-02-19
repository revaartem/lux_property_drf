from django.contrib import admin
from .models import ContactUs, ContactInfoLeft, Sources, MediaLinks

# Register your models here.
admin.site.register(ContactUs)
admin.site.register(Sources)
admin.site.register(MediaLinks)


@admin.register(ContactInfoLeft)
class ContactInfoLeftAdmin(admin.ModelAdmin):
    list_display = ['location', 'open_hours', 'email', 'call', ]
    list_editable = ['open_hours', 'email', 'call', ]