import time

from django.shortcuts import render, redirect

from contact_us.forms import ContactForm
from contact_us.models import ContactInfoLeft


# Create your views here.


def confirmation(request):
    """
    Renders the confirmation page.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        HttpResponse: The rendered confirmation page.
    """

    return render(request, 'confirmation_page.html')


def contact_us_view(request):
    """
    Renders the contact page with contact form and left information.

    If a valid POST request is made, it saves the contact form and redirects
    to the confirmation page.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        HttpResponse: The rendered contact page.
    """

    if request.method == 'POST':
        contact_us = ContactForm(request.POST)
        if contact_us.is_valid():
            contact_us.save()
            return redirect('contact_us:confirmation')

    contact_form = ContactForm()
    left_information = ContactInfoLeft.objects.all()

    data = {
        'contact_form': contact_form,
        'left_information': left_information,
    }

    return render(request, 'contact_page_structure.html', context=data)


