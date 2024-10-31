from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from authentication.serializers import LoginSerializer
from base.utils.response_utils import create_response, error_response
from base.utils.decorators import handle_exceptions
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class LoginView(APIView):
    permission_classes = [AllowAny]

    @handle_exceptions
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            # Authenticate using custom user model
            user = authenticate(username=username, password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return create_response(
                    data={
                        "refresh": str(refresh), 
                        "access": str(refresh.access_token)
                    }, 
                    message="Login successful"
                )
            return error_response("Invalid credentials", status_code=401)

        return error_response(serializer.errors, status_code=400)
