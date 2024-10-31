from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from authentication.models import BlacklistedToken

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Extract the token from the Authorization header
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if auth_header is None:
            return Response({"detail": "Authorization header is missing."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            token = auth_header.split()[1]  # Bearer <token>
        except IndexError:
            return Response({"detail": "Invalid token format."}, status=status.HTTP_400_BAD_REQUEST)

        # Blacklist the token
        BlacklistedToken.objects.create(token=token)

        return Response({"Status": "Logout successful."}, status=status.HTTP_200_OK)
