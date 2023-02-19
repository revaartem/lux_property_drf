from django.shortcuts import render, redirect
from .forms import UserLogin
from django.contrib.auth import login, authenticate, logout


# Create your views here.
def login_view(request):
    """
    View function of the login page. Processed POST and GET requests.

    form - form from model UserLogin with GET request or None.\n
    next_get - Next page parameters.\n
    information_in_contact_us - Object model InformationInContactUs.\n
    footer - footer - Footer object model.\n
    user_manager - Checked if user have group 'manager' in his group list.\n
    user_auth - Is user authenticated or not.\n

    :param request: POST or GET request.
    :return: Render of the HTML-page with context.
    """
    form = UserLogin(request.POST or None)
    next_get = request.GET.get('next')
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)

        next_post = request.POST.get('next')
        return redirect(next_get or next_post or '/')

    data = {
        'form': form,
    }

    return render(request, 'login_form.html', context=data)


def logout_view(request):
    """
    Logout view.

    :param request: GET request.
    :return: Redirect to the main page.
    """
    logout(request)
    return redirect('main_page:main_page_view')
