from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from authentication.serializers import PasswordReset, PasswordResetSerializer
from base.utils.response_utils import create_response, error_response
from base.utils.decorators import handle_exceptions


class PasswordResetConfirmView(APIView):
    permission_classes = [AllowAny]

    @handle_exceptions
    def post(self, request, token):
        serializer = PasswordResetSerializer(data={"token": token, "new_password": request.data.get("new_password")})
        if serializer.is_valid():
            password_reset = PasswordReset.objects.get(token=token)
            user = password_reset.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            password_reset.is_used = True
            password_reset.save()
            return create_response(message="Password reset successful")
        return error_response(serializer.errors)