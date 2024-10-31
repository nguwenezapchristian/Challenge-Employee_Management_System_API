from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from authentication.serializers import ForgotPasswordSerializer, PasswordReset
from base.utils.response_utils import create_response, error_response
from base.utils.decorators import handle_exceptions
from django.utils import timezone
import uuid
from authentication.models import User
from base.utils.email_service import EmailService


class ForgotPasswordView(APIView):
    permission_classes = [AllowAny]
    email_service = EmailService()  # Create an instance of the email service

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
                
                # Send password reset email
                reset_link = f"{request.scheme}://{request.get_host()}/reset-password/{token}/"
                subject = "Password Reset Request"
                text_body = f"Hi {user.username},\n\nTo reset your password, use the following link:\n{reset_link}\n\nThis link will expire in 1 hour."
                html_body = f"<p>Hi {user.username},</p><p>To reset your password, use the following link: <a href='{reset_link}'>Reset Password</a>.</p><p>This link will expire in 1 hour.</p>"

                self.email_service.send_email(email, subject, text_body, html_body)
                
                return create_response(message="Password reset email sent.")
            return error_response("Email not found", status_code=404)
        return error_response(serializer.errors)
