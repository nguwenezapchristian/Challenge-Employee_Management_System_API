from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from base.utils.decorators import handle_exceptions
from base.utils.response_utils import create_response
from employees.serializers import EmployeeCreateSerializer, EmployeeSerializer
from employees.models import Employee
from authentication.models import User
from django.db import transaction

class CreateEmployeeView(APIView):
    permission_classes = [AllowAny]
    queryset = Employee.objects.all()
    @handle_exceptions
    @transaction.atomic
    def post(self, request):
        """
        Create a new employee with user account
        """
        serializer = EmployeeCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Extract password from validated data
        password = serializer.validated_data.pop('password')
        
        # Create user account for employee
        user = User.objects.create_user(
            username=serializer.validated_data['email'],
            email=serializer.validated_data['email'],
            password=password,
            role='employee'
        )
        
        # Create employee profile
        employee = Employee.objects.create(
            user=user,
            **serializer.validated_data
        )
        
        return create_response(
            data=EmployeeSerializer(employee).data,
            message="Employee created successfully",
            status_code=status.HTTP_201_CREATED
        )