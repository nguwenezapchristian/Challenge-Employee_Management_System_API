from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from base.utils.decorators import handle_exceptions
from base.utils.response_utils import create_response
from base.utils.exceptions import ResourceNotFound
from employees.serializers import EmployeeSerializer
from employees.models import Employee
from django.db.models import Q


class RetrieveEmployeeView(APIView):
    permission_classes = [AllowAny]
    queryset = Employee.objects.all()

    @handle_exceptions
    def get(self, request, employee_id=None):
        """
        Retrieve employee by ID or employee_id
        """
        try:
            # Try to find by UUID first, then by employee_id
            query = Q(id=employee_id) if len(employee_id) > 10 else Q(employee_id=employee_id)
            employee = Employee.objects.get(query)
            
            return create_response(
                data=EmployeeSerializer(employee).data,
                message="Employee retrieved successfully"
            )
        except Employee.DoesNotExist:
            raise ResourceNotFound("Employee not found")

class ListEmployeesView(APIView):
    permission_classes = [AllowAny]
    queryset = Employee.objects.all()

    @handle_exceptions
    def get(self, request):
        """
        List all employees with optional search and pagination
        """
        # Retrieve search query without quotes
        search_query = request.query_params.get('search', '').strip('"')
        page = int(request.query_params.get('page', 1))
        limit = int(request.query_params.get('limit', 10))

        # Apply filtering
        queryset = Employee.objects.filter(
            Q(name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(employee_id__icontains=search_query)
        )

        # Check if there are matching results
        if not queryset.exists():
            return create_response(
                success=False,
                message="Employee not found",
                data=None,
                status=status.HTTP_404_NOT_FOUND
            )

        # Pagination
        start = (page - 1) * limit
        end = start + limit
        employees = queryset[start:end]
        total = queryset.count()

        return create_response(
            data={
                'employees': EmployeeSerializer(employees, many=True).data,
                'total': total,
                'page': page,
                'total_pages': (total + limit - 1) // limit
            },
            message="Employees retrieved successfully"
        )

