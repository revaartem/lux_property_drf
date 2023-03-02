from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import HeroHeader, HeroBackgroundPhotos, Realtor, Property, PropertyPhoto, OurBenefits, CustomerSays
from .serializers import HeroHeaderSerializer, HeroBackgroundPhotosSerializer, RealtorSerializer, PropertySerializer,\
    PropertyPhotoSerializer, OurBenefitsSerializer, CustomerSaysSerializer

from manager.models import BackgroundImagesForPages
from manager.serializers import BackgroundImagesForPagesSerializer, SessionPathSerializer,\
    UnprocessedApplicationsSerializer

from contact_us.models import ContactUs, ContactInfoLeft, Sources, MediaLinks
from contact_us.serializers import ContactInfoLeftSerializer, SourcesSerializer,\
    MediaLinksSerializer


def context_func(request):

    bg_photos = BackgroundImagesForPages.objects.all()
    bg_photos_serializer = BackgroundImagesForPagesSerializer(bg_photos, many=True)

    session_path_serializer = SessionPathSerializer({'path': request.path})

    contact_applications = len(ContactUs.objects.filter(is_processed=False))
    contact_applications_serializer = UnprocessedApplicationsSerializer({'unprocessed': contact_applications})

    infos = ContactInfoLeft.objects.all()
    infos_serializer = ContactInfoLeftSerializer(infos, many=True)

    sources = Sources.objects.all()
    sources_serializer = SourcesSerializer(sources, many=True)

    media_links_blocks = MediaLinks.objects.all()
    media_links_blocks_serializer = MediaLinksSerializer(media_links_blocks, many=True)

    data = {
        'bg_photos': bg_photos_serializer.data,
        'path': session_path_serializer.data,
        'contact_applications': contact_applications_serializer.data,
        'infos': infos_serializer.data,
        'sources': sources_serializer.data,
        'media_links_blocks': media_links_blocks_serializer.data,
    }

    return data


@api_view(['GET', 'POST'])
def all_data(request):
    if request.method == 'GET':

        hero_header = HeroHeader.objects.all()
        hero_header_serializer = HeroHeaderSerializer(hero_header, many=True)

        hero_background_photos_data = HeroBackgroundPhotos.objects.all()
        hero_background_photos_serializer = HeroBackgroundPhotosSerializer(hero_background_photos_data, many=True)

        realtor_data = Realtor.objects.all()
        realtor_serializer = RealtorSerializer(realtor_data, many=True)

        property_data = Property.objects.all()
        property_serializer = PropertySerializer(property_data, many=True)

        property_photo_data = PropertyPhoto.objects.all()
        property_photo_serializer = PropertyPhotoSerializer(property_photo_data, many=True)

        our_benefits_data = OurBenefits.objects.all()
        our_benefits_serializer = OurBenefitsSerializer(our_benefits_data, many=True)

        customer_says_data = CustomerSays.objects.all()
        customer_says_serializer = CustomerSaysSerializer(customer_says_data, many=True)

        result = {
            'hero_header': hero_header_serializer.data,
            'hero_background_photos': hero_background_photos_serializer.data,
            'realtor': realtor_serializer.data,
            'property': property_serializer.data,
            'property_photo': property_photo_serializer.data,
            'our_benefits': our_benefits_serializer.data,
            'customer_says': customer_says_serializer.data,
            'context': context_func(request),
        }

        return Response(result)

    elif request.method == 'POST':
        # Обработка POST-запроса здесь
        pass

