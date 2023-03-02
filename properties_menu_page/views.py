from rest_framework.decorators import api_view
from rest_framework.response import Response
from main_page.serializers import PropertySerializer, PropertyPhotoSerializer
from main_page.models import Property, PropertyPhoto
from main_page.views import context_func

@api_view(['GET', ])
def property_menu_data(request):
    if request.method == 'GET':
        property_all_items = Property.objects.filter(is_visible=True)
        property_all_serializer = PropertySerializer(property_all_items, many=True)

        property_special_items = Property.objects.filter(is_visible=True, recommended_offer=True)
        property_special_serializer = PropertySerializer(property_special_items, many=True)

        property_photo_data = PropertyPhoto.objects.all()
        property_photo_serializer = PropertyPhotoSerializer(property_photo_data, many=True)

        result = {
            'property_all': property_all_serializer.data,
            'property_special': property_special_serializer.data,
            'property_photos': property_photo_serializer.data,
            'context': context_func(request),

        }

        return Response(result)
