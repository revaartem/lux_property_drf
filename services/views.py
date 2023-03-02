from django.shortcuts import render, get_object_or_404
from .models import ServicesInfoOffer
from main_page.models import CustomerSays
from main_page.serializers import CustomerSaysSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ServicesInfoOfferSerializer
from main_page.views import context_func


@api_view(['GET', ])
def services_view(request):
    if request.method == 'GET':
        info_blocks = ServicesInfoOffer.objects.filter(is_visible=True)
        info_blocks_serializer = ServicesInfoOfferSerializer(info_blocks, many=True)

        customers = CustomerSays.objects.filter(is_visible=True)
        customers_serializer = CustomerSaysSerializer(customers, many=True)

        data = {
            'info_blocks': info_blocks_serializer.data,
            'customers': customers_serializer.data,
            'context': context_func(request),
        }

        return Response(data)


@api_view(['GET', ])
def services_direct_view(request, id, slug):
    if request.method == 'GET':
        info_block = get_object_or_404(ServicesInfoOffer, id=id, slug=slug, is_visible=True)
        info_blocks_serializer = ServicesInfoOfferSerializer(info_block)

        data = {
            'info_block': info_blocks_serializer.data,
            'context': context_func(request),
        }

        return Response(data)
