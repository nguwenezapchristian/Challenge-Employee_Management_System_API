from rest_framework import serializers
from authentication.models import User, PasswordReset
from django.contrib.auth.password_validation import validate_password
from django.core.validators import EmailValidator
from django.utils import timezone

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    email = serializers.EmailField(validators=[EmailValidator()])

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'role')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data['role']
        )
        user.is_email_verified = False
        user.save()
        return user


class LogoutSerializer(serializers.Serializer):
    message = serializers.CharField(default='Logout successful.')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordResetSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True, validators=[validate_password])

    def validate(self, data):
        user_reset = PasswordReset.objects.filter(token=data['token'], is_used=False).first()
        if not user_reset or user_reset.expires_at < timezone.now():
            raise serializers.ValidationError("Invalid or expired token")
        return data
