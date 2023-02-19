from django.contrib import admin
from main_page.models import HeroHeader, HeroBackgroundPhotos, Realtor, PropertyPhoto, Property, OurBenefits, \
    CustomerSays

# Register your models here.


@admin.register(HeroHeader)
class HeroHeaderAdmin(admin.ModelAdmin):
    """
    Customizes the HeroHeader model's representation in Django Admin.

    Allows for editing the text of the hero header on the website.

    Attributes:
    -----------
    list_display : tuple
        A tuple containing fields to be displayed in the list view of the model.
    """

    list_display = ['text']


admin.site.register(HeroBackgroundPhotos)


@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    """
    Customizes the Realtor model's representation in Django Admin.

    Allows for editing the realtors and their details displayed on the Our Agents page.

    Attributes:
    -----------
    list_display : tuple
        A tuple containing fields to be displayed in the list view of the model.
    """

    list_display = ['name', 'position', 'short_about']


class PropertyPhotoAdmin(admin.TabularInline):
    """
    Customizes the PropertyPhoto model's representation in Django Admin.

    Allows for adding and editing photos associated with a specific property.

    Attributes:
    -----------
    model : class
        The model associated with the inline.
    raw_id_fields : list
        A list of fields to be displayed as raw id fields.
    """

    model = PropertyPhoto
    raw_id_fields = ['property_item']


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    """
    Customizes the Property model's representation in Django Admin.

    Allows for adding and editing properties displayed on the website.

    Attributes:
    -----------
    prepopulated_fields : dict
        A dictionary of fields whose value will be automatically set using another field's value.
    inlines : list
        A list of inline models to be displayed on the property page.
    list_filter : tuple
        A tuple containing fields to be displayed as filters in the list view of the model.
    list_display : tuple
        A tuple containing fields to be displayed in the list view of the model.
    list_editable : tuple
        A tuple containing fields that can be edited in the list view of the model.
    """

    prepopulated_fields = {'slug': ('name', ), }
    inlines = [PropertyPhotoAdmin]
    list_filter = ('is_visible', 'recommended_offer', 'country', 'realtor')
    list_display = ['name', 'is_visible', 'recommended_offer', 'location_address', 'country', 'realtor']
    list_editable = ['is_visible', 'recommended_offer', ]


@admin.register(OurBenefits)
class OurBenefitsAdmin(admin.ModelAdmin):
    """
    Customizes the OurBenefits model's representation in Django Admin.

    Allows for adding and editing benefits and associated details displayed on the website.

    Attributes:
    -----------
    list_display : tuple
        A tuple containing fields to be displayed in the list view of the model.
    """
    list_display = ['header', 'heading_text', 'image']


@admin.register(CustomerSays)
class CustomerSaysAdmin(admin.ModelAdmin):
    """
    Customizes the CustomerSays model's representation in Django Admin.

    Allows for adding and editing customer testimonials and associated details displayed on the website.

    Attributes:
    -----------
    list_display : tuple
        A tuple containing fields to be displayed in the list view of the model.
    list_editable : tuple
        A tuple containing fields that can be edited in the list view of the model.
    """
    list_display = ['name', 'is_visible', 'comment', 'customer_position']
    list_editable = ['is_visible', ]
