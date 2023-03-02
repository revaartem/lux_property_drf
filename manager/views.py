from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required, user_passes_test
from contact_us.models import ContactUs
from contact_us.serializers import ContactUsSerializer
from rest_framework import status
# Create your views here.


def is_manager(user):
    """
    A helper function that returns True if the user belongs to the 'manager' group, False otherwise.
    """
    return user.groups.filter(name='manager').exists()


@login_required(login_url='login/')
@user_passes_test(is_manager)
@api_view(['GET', ])
def manager_view(request):
    """
    View function that displays the manager menu content page, including a list of processed and unprocessed contact
    us forms.

    Access is only granted to users who belong to the 'manager' group.

    :param request: The HTTP request.
    :return: The HTTP response that represents the manager menu content page.
    """
    processed = ContactUs.objects.filter(is_processed=True)
    processed_serializer = ContactUsSerializer(processed, many=True)

    unprocessed = ContactUs.objects.filter(is_processed=False)
    unprocessed_serializer = ContactUsSerializer(unprocessed, many=True)

    data = {
        'processed': processed_serializer.data,
        'unprocessed': unprocessed_serializer.data,
    }

    return Response(data)


@login_required(login_url='login/')
@user_passes_test(is_manager)
@api_view(['GET', ])
def archived_applications(request):
    """
    View function that displays the archived applications page, including a list of processed contact us forms.

    Access is only granted to users who belong to the 'manager' group.

    :param request: The HTTP request.
    :return: The HTTP response that represents the archived applications page.
    """

    processed = ContactUs.objects.filter(is_processed=True)
    processed_serializer = ContactUsSerializer(processed, many=True)

    data = {
        'processed': processed_serializer.data,
    }

    return Response(data)


@login_required(login_url='login/')
@user_passes_test(is_manager)
@api_view(['GET', ])
def new_applications(request):
    """
    View function that displays the new applications page, including a list of unprocessed contact us forms.

    Access is only granted to users who belong to the 'manager' group.

    :param request: The HTTP request.
    :return: The HTTP response that represents the new applications page.
    """

    unprocessed = ContactUs.objects.filter(is_processed=False)
    unprocessed_serializer = ContactUsSerializer(unprocessed, many=True)

    data = {
        'unprocessed': unprocessed_serializer.data,
    }
    return Response(data)


@login_required(login_url='login/')
@user_passes_test(is_manager)
@api_view(['GET', ])
def application_to_archive(request, pk):
    """
    View function that archives a contact us form with the specified primary key.

    Access is only granted to users who belong to the 'manager' group.

    :param request: The HTTP request.
    :param pk: The primary key of the contact us form to archive.
    :return: The HTTP response that represents the new applications page.
    """
    ContactUs.objects.filter(pk=pk).update(is_processed=True)
    return Response(status=status.HTTP_200_OK)


@login_required(login_url='login/')
@user_passes_test(is_manager)
@api_view(['GET', ])
def delete_application(request, pk):
    """
    View function that deletes a contact us form with the specified primary key.

    Access is only granted to users who belong to the 'manager' group.

    :param request: The HTTP request.
    :param pk: The primary key of the contact us form to delete.
    :return: The HTTP response that represents the archived applications page.
    """
    ContactUs.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)
