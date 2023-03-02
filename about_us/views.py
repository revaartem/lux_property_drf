from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import AboutUsTopInfo, FirstBenefitsBlock, SecondBenefitsBlock, PhotosAndNumbers, TeamMember
from .serializers import AboutUsTopInfoSerializer, FirstBenefitsBlockSerializer, SecondBenefitsBlockSerializer,\
    PhotosAndNumbersSerializer, TeamMemberSerializer
from main_page.views import context_func


@api_view(['GET', ])
def about_us_view(request):
    """
    View function that handles GET requests for the 'about us' page.
    Returns serialized data for the AboutUsTopInfo, FirstBenefitsBlock, SecondBenefitsBlock,
    PhotosAndNumbers, and TeamMember models, as well as the result of the context_func function.

    :param request: GET request object.
    :return: Response object with serialized data and context.
    """
    if request.method == 'GET':
        info_block = AboutUsTopInfo.objects.all()
        info_block_serializer = AboutUsTopInfoSerializer(info_block, many=True)

        first_benefits = FirstBenefitsBlock.objects.all()
        first_benefits_serializer = FirstBenefitsBlockSerializer(first_benefits, many=True)

        second_benefits = SecondBenefitsBlock.objects.all()
        second_benefits_serializer = SecondBenefitsBlockSerializer(second_benefits, many=True)

        photos_and_numbers = PhotosAndNumbers.objects.all()
        photos_and_numbers_serializer = PhotosAndNumbersSerializer(photos_and_numbers, many=True)

        team_members = TeamMember.objects.filter(visible_in_our_agents=True)
        team_members_serializer = TeamMemberSerializer(team_members, many=True)

        data = {
            'info_block': info_block_serializer.data,
            'first_benefits': first_benefits_serializer.data,
            'second_benefits': second_benefits_serializer.data,
            'photos_and_numbers': photos_and_numbers_serializer.data,
            'team_members': team_members_serializer.data,
            'context': context_func(request),
        }

        return Response(data)
