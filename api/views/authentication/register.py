from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from authentication.serializers import RegisterSerializer
from base.utils.response_utils import create_response, error_response
from base.utils.decorators import handle_exceptions


class RegisterView(APIView):
    permission_classes = [AllowAny]

    @handle_exceptions
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return create_response(data={"user_id": user.id}, message="User registered successfully")
        return error_response(serializer.errors)