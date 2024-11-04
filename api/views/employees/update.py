from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from base.permissions import IsAdminUser
from base.utils.decorators import handle_exceptions
from base.utils.response_utils import create_response
from base.utils.exceptions import ResourceNotFound
from employees.serializers import EmployeeSerializer
from employees.models import Employee

class UpdateEmployeeView(APIView):
    # permission_classes = [IsAuthenticated] # change this line in production
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Employee.objects.all()
    @handle_exceptions
    def put(self, request, employee_id):
        try:
            employee = Employee.objects.get(employee_id=employee_id)
            serializer = EmployeeSerializer(
                employee,
                data=request.data,
                partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            
            return create_response(
                data=serializer.data,
                message="Employee updated successfully"
            )
        except Employee.DoesNotExist:
            raise ResourceNotFound("Employee not found")