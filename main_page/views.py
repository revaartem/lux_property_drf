from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template.defaulttags import register


from main_page.models import HeroHeader, HeroBackgroundPhotos, Property, PropertyPhoto, OurBenefits, CustomerSays,\
    Realtor

# Create your views here.


def main_page_view(request: HttpRequest) -> HttpResponse:
    """
    This view function renders the main page of the website.

    It retrieves information about the hero header, hero background photos, featured property,
    all property photos, our benefits, customer reviews, and our real estate agents, and passes
    this data to the main_page.html template to be rendered.

    :param request: The HTTP request object.
    :return: The HTTP response object.
    """
    hero_header = HeroHeader.objects.all()
    hero_photos = HeroBackgroundPhotos.objects.filter(is_visible=True)
    house_item = Property.objects.filter(is_visible=True, recommended_offer=True).all()
    photos_item = PropertyPhoto.objects.all()
    benefits = OurBenefits.objects.all()
    customers = CustomerSays.objects.filter(is_visible=True)
    realtors = Realtor.objects.filter(visible_in_our_agents=True)

    data = {

        'hero_header': hero_header,
        'hero_photos': hero_photos,
        'house_item': house_item,
        'photos_item': photos_item,
        'benefits': benefits,
        'customers': customers,
        'realtors': realtors

    }
    return render(request, 'main_page.html', context=data)
