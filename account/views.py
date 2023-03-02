from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from .serializers import UserLoginSerializer
from rest_framework.decorators import api_view


class LoginView(APIView):
    """
    View function of the login page. Processed POST requests.
    """
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({'success': True}, status=status.HTTP_200_OK)
            else:
                return Response({'success': False, 'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def logout_view(request):
    """
    Logout view.

    :param request: GET request.
    :return: Response with status 200.
    """
    logout(request)
    return Response(status=status.HTTP_200_OK)