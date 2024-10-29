from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from base.utils.decorators import handle_exceptions
from base.utils.response_utils import create_response
from base.utils.exceptions import ResourceNotFound
from employees.models import Employee

class DeleteEmployeeView(APIView):
    # permission_classes = [IsAuthenticated] # change this line in production
    permission_classes = [AllowAny]
    queryset = Employee.objects.all()
    @handle_exceptions
    def delete(self, request, employee_id):
        try:
            employee = Employee.objects.get(employee_id=employee_id)
            employee.is_active = False
            employee.save()
            
            # Optionally, deactivate associated user account
            if employee.user:
                employee.user.is_active = False
                employee.user.save()
            
            return create_response(
                message="Employee deleted successfully",
                status_code=status.HTTP_204_NO_CONTENT
            )
        except Employee.DoesNotExist:
            raise ResourceNotFound("Employee not found")