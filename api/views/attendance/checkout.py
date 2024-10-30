from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from base.utils.decorators import handle_exceptions
from base.utils.response_utils import create_response
from attendance.models import Attendance
from employees.models import Employee
from django.utils import timezone
from django.shortcuts import get_object_or_404

class CheckOutView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    @handle_exceptions
    def post(self, request, employee_id):
        employee = get_object_or_404(Employee, employee_id=employee_id)
        attendance = Attendance.objects.filter(employee=employee, check_out_time__isnull=True).first()

        if not attendance:
            return create_response(
                message="No active attendance record found.",
                status_code=status.HTTP_400_BAD_REQUEST
            )

        attendance.check_out_time = timezone.now()
        attendance.save()

        return create_response(
            data={'check_out_time': attendance.check_out_time},
            message="Checked out successfully.",
            status_code=status.HTTP_200_OK
        )
