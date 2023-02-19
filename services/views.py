from django.shortcuts import render, get_object_or_404
from .models import ServicesInfoOffer
from main_page.models import CustomerSays
# Create your views here.


def services_view(request):
    """
    View function for displaying the services page.

    Retrieves all services that are set to be visible and customer feedbacks from the database, and renders them on the
    services page.

    Parameters:
        request (HttpRequest): The HTTP request object that is used to generate the response.

    Returns:
        HttpResponse: The HTTP response object that contains the rendered HTML content of the services page.

    Variables:
        info_blocks (QuerySet): A QuerySet of all ServicesInfoOffer objects that have is_visible attribute set to True.
        customers (QuerySet): A QuerySet of all CustomerSays objects that have is_visible attribute set to True.
        data (dict): A dictionary that contains the info_blocks and customers QuerySets, to be passed to the
        services_all_page_structure.html template.
    """

    info_blocks = ServicesInfoOffer.objects.filter(is_visible=True)
    customers = CustomerSays.objects.filter(is_visible=True)

    data = {
        'info_blocks': info_blocks,
        'customers': customers,
    }

    return render(request, 'services_all_page_structure.html', context=data)


def services_direct_view(request, id, slug):
    """
    View function for displaying a single service on a page.

    Retrieves a single service from the database based on the provided id and slug, and renders it on the
    services_single_content.html page.

    Parameters:
        request (HttpRequest): The HTTP request object that is used to generate the response.
        id (int): The id of the ServicesInfoOffer object that is to be displayed.
        slug (str): The slug of the ServicesInfoOffer object that is to be displayed.

    Returns:
        HttpResponse: The HTTP response object that contains the rendered HTML content of the single service page.

    Variables:
        info_block (ServicesInfoOffer): The ServicesInfoOffer object that matches the provided id and slug parameters.
        data (dict): A dictionary that contains the info_block object, to be passed to the services_single_content.html
        template.
    """

    info_block = get_object_or_404(ServicesInfoOffer, id=id, slug=slug, is_visible=True)

    data = {
        'info_block': info_block,
    }

    return render(request, 'services_single_content.html', context=data)
