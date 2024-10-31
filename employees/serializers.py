from rest_framework import serializers
from .models import Employee
from .services.employee_service import EmployeeService
from authentication.models import User
from django.contrib.auth.password_validation import validate_password

class EmployeeCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    email = serializers.EmailField(required=True)
    
    class Meta:
        model = Employee
        fields = (
            'name', 
            'email', 
            'phone_number', 
            'password',
        )

    def validate_email(self, value):
        # Check if email exists in User model
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'name', 
            'email', 
            'employee_id', 
            'phone_number', 
            'created_at', 
            'updated_at'
        )
        read_only_fields = ('employee_id',)