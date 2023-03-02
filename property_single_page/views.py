from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from main_page.models import Property, PropertyPhoto
from main_page.serializers import PropertySerializer, PropertyPhotoSerializer
from main_page.views import context_func


@api_view(['GET', ])
def single_page_view(request, id, slug):
    if request.method == 'GET':
        property_ = get_object_or_404(Property, id=id, slug=slug, is_visible=True)
        property_all_serializer = PropertySerializer(property_)

        photo = PropertyPhoto.objects.filter(property_item=property_)
        property_photo_serializer = PropertyPhotoSerializer(photo, many=True)

        data = {
            'property_': property_all_serializer.data,
            'photo': property_photo_serializer.data,
            'context': context_func(request),
        }

        return Response(data)
