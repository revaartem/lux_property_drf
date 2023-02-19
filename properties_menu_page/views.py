from django.shortcuts import render
from main_page.models import Property, PropertyPhoto


# Create your views here.


def property_menu_view(request):
    """
    View function that displays the property menu page with featured and regular offers.

    Returns:
    Renders the 'menu_page.html' template with the following context:
    - 'featured_item': QuerySet of featured properties that are visible and have a recommended offer status.
    - 'regular_item': QuerySet of regular properties that are visible.
    - 'photos_item': QuerySet of all property photos.
    """

    featured_item = Property.objects.filter(is_visible=True, recommended_offer=True)
    regular_item = Property.objects.filter(is_visible=True)
    photos_item = PropertyPhoto.objects.all()

    data = {
        'featured_item': featured_item,
        'regular_item': regular_item,
        'photos_item': photos_item

    }

    return render(request, 'menu_page.html', context=data)
