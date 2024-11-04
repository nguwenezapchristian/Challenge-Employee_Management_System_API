from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from base.permissions import IsAdminUser
from base.utils.decorators import handle_exceptions
from base.utils.response_utils import create_response
from employees.serializers import EmployeeCreateSerializer, EmployeeSerializer
from employees.models import Employee
from authentication.models import User
from django.db import transaction

class CreateEmployeeView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Employee.objects.all()

    @handle_exceptions
    @transaction.atomic
    def post(self, request):
        """
        Create a new employee with user account
        """
        # Extract email from request data
        email = request.data.get('email')
        
        # Check for an existing inactive employee
        existing_employee = Employee.objects.filter(email=email, is_active=False).first()
        if existing_employee:
            # Reactivate the existing employee
            existing_employee.is_active = True
            existing_employee.save()

            return create_response(
                data=EmployeeSerializer(existing_employee).data,
                message="Employee reactivated successfully",
                status_code=status.HTTP_200_OK
            )

        # Proceed with serializer validation and creation for a new employee
        serializer = EmployeeCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Extract password from validated data
        password = serializer.validated_data.pop('password')

        # Create user account for the new employee
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            role='employee'
        )

        # Create employee profile
        new_employee = Employee.objects.create(
            user=user,
            **serializer.validated_data
        )

        return create_response(
            data=EmployeeSerializer(new_employee).data,
            message="Employee created successfully",
            status_code=status.HTTP_201_CREATED
        )
