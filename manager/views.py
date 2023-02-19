from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from contact_us.models import ContactUs
# Create your views here.


def is_manager(user):
    """
    A helper function that returns True if the user belongs to the 'manager' group, False otherwise.
    """
    return user.groups.filter(name='manager').exists()


@login_required(login_url='login/')
@user_passes_test(is_manager)
def manager_view(request):
    """
    View function that displays the manager menu content page, including a list of processed and unprocessed contact
    us forms.

    Access is only granted to users who belong to the 'manager' group.

    :param request: The HTTP request.
    :return: The HTTP response that represents the manager menu content page.
    """
    processed = ContactUs.objects.filter(is_processed=True)
    unprocessed = ContactUs.objects.filter(is_processed=False)

    data = {
        'processed': processed,
        'unprocessed': unprocessed,
    }

    return render(request, 'manager_menu_content.html', context=data)


@login_required(login_url='login/')
@user_passes_test(is_manager)
def archived_applications(request):
    """
    View function that displays the archived applications page, including a list of processed contact us forms.

    Access is only granted to users who belong to the 'manager' group.

    :param request: The HTTP request.
    :return: The HTTP response that represents the archived applications page.
    """

    processed = ContactUs.objects.filter(is_processed=True)

    data = {
        'processed': processed,
    }

    return render(request, 'archived_applications.html', context=data)


@login_required(login_url='login/')
@user_passes_test(is_manager)
def new_applications(request):
    """
    View function that displays the new applications page, including a list of unprocessed contact us forms.

    Access is only granted to users who belong to the 'manager' group.

    :param request: The HTTP request.
    :return: The HTTP response that represents the new applications page.
    """

    unprocessed = ContactUs.objects.filter(is_processed=False)
    data = {
        'unprocessed': unprocessed,
    }
    return render(request, 'unprocessed_applications.html', context=data)


@login_required(login_url='login/')
@user_passes_test(is_manager)
def application_to_archive(request, pk):
    """
    View function that archives a contact us form with the specified primary key.

    Access is only granted to users who belong to the 'manager' group.

    :param request: The HTTP request.
    :param pk: The primary key of the contact us form to archive.
    :return: The HTTP response that represents the new applications page.
    """
    ContactUs.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:new_applications')


@login_required(login_url='login/')
@user_passes_test(is_manager)
def delete_application(request, pk):
    """
    View function that deletes a contact us form with the specified primary key.

    Access is only granted to users who belong to the 'manager' group.

    :param request: The HTTP request.
    :param pk: The primary key of the contact us form to delete.
    :return: The HTTP response that represents the archived applications page.
    """
    ContactUs.objects.filter(pk=pk).delete()
    return redirect('manager:archived_applications')
