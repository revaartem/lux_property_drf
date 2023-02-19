from django.shortcuts import render, get_object_or_404
from main_page.models import Property, PropertyPhoto, Realtor

# Create your views here.


def single_page_view(request, id, slug):
    """
    View function for displaying a single property page.

    Args:
        request (HttpRequest): The HTTP request object sent by the client.
        id (int): The unique ID of the property to be displayed.
        slug (str): The slugified version of the property's title.

    Returns:
        HttpResponse: An HTTP response object containing the rendered HTML for the property page.

    Raises:
        Http404: If no Property object with the given ID and slug is found.

    Variables:
        property_ (Property): The Property object to be displayed on the page.
        photo (QuerySet): A queryset of all the photos associated with the property.
        realtor (Realtor): The Realtor object associated with the property.
        font_pic (QuerySet): A queryset of all the font images associated with the property page.
    """

    property_ = get_object_or_404(Property, id=id, slug=slug, is_visible=True)
    photo = PropertyPhoto.objects.filter(property_item=property_).all()
    realtor = Realtor.objects.filter(name=property_.realtor.name).get()
    font_pic = PropertyPhoto.objects.filter(property_item=property_).filter(font_image_of_offer_page=True).all()

    data = {
        'property_': property_,
        'photo': photo,
        'realtor': realtor,
        'font_pic': font_pic,

    }

    return render(request, 'property_page_structure.html', context=data)
