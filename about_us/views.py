from django.shortcuts import render
from .models import AboutUsTopInfo, FirstBenefitsBlock, SecondBenefitsBlock, PhotosAndNumbers, TeamMember

# Create your views here.


def about_us_view(request):
    """
    View function to render the about us page.

    Args:
    request (HttpRequest): The HTTP request sent to the server.

    Returns:
        HttpResponse: The HTTP response containing the rendered about us page.
    """

    info_block = AboutUsTopInfo.objects.all()
    first_benefits = FirstBenefitsBlock.objects.all()
    second_benefits = SecondBenefitsBlock.objects.all()
    photos_and_numbers = PhotosAndNumbers.objects.all()
    team_members = TeamMember.objects.filter(visible_in_our_agents=True)

    data = {
        'info_block': info_block,
        'first_benefits': first_benefits,
        'second_benefits': second_benefits,
        'photos_and_numbers': photos_and_numbers,
        'team_members': team_members,
    }

    return render(request, 'about_us_content_structure.html', context=data)