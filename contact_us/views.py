import time

from rest_framework.decorators import api_view
from rest_framework.response import Response
from contact_us.models import ContactInfoLeft, ContactUs, Sources, MediaLinks
from .serializers import ContactUsSerializer, ContactInfoLeftSerializer, SourcesSerializer, MediaLinksSerializer
from main_page.views import context_func


@api_view(['GET', 'POST'])
def contact_us_view(request):
    """
    API endpoint for handling contact form submissions.

    GET request returns the serialized data for ContactInfoLeft, Sources, and MediaLinks models and context
    for rendering the contact form.

    POST request accepts form data in JSON format, validates it using the ContactUsSerializer, saves the
    data to the ContactUs model, and returns a success message along with the id of the newly created
    ContactUs instance.

    :param request: HTTP request object
    :type request: rest_framework.request.Request

    :return: HTTP response object
    :rtype: rest_framework.response.Response
    """

    if request.method == 'POST':
        data_serializer = ContactUsSerializer(data=request.data)
        if data_serializer.is_valid():
            contact_form = data_serializer.save()
            return Response({'status': 'success', 'id': contact_form.id})
        return Response(data_serializer.errors, status=400)

    if request.method == 'GET':
        contact_info_left = ContactInfoLeft.objects.all()
        contact_info_left_serializer = ContactInfoLeftSerializer(contact_info_left, many=True)

        sources = Sources.objects.all()
        sources_serializer = SourcesSerializer(sources, many=True)

        media_links = MediaLinks.objects.all()
        media_links_serializer = MediaLinksSerializer(media_links, many=True)

        data = {
            'contact_info_left': contact_info_left_serializer.data,
            'sources': sources_serializer.data,
            'media_links': media_links_serializer.data,
            'context': context_func(request),
        }

        return Response(data)


