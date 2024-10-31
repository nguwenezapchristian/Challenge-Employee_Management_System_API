from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from authentication.serializers import ForgotPasswordSerializer, PasswordReset
from base.utils.response_utils import create_response, error_response
from base.utils.decorators import handle_exceptions
from django.utils import timezone
import uuid
from authentication.models import User


class ForgotPasswordView(APIView):
    permission_classes = [AllowAny]

    @handle_exceptions
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = User.objects.filter(email=email).first()
            if user:
                # Create password reset token logic
                token = str(uuid.uuid4())
                expires_at = timezone.now() + timezone.timedelta(hours=1)
                PasswordReset.objects.create(user=user, token=token, expires_at=expires_at)
                # Send email with token (implementation of email sending is not covered)
                return create_response(message="Password reset email sent.")
            return error_response("Email not found", status_code=404)
        return error_response(serializer.errors)