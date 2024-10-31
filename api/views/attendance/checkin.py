from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from base.utils.decorators import handle_exceptions
from base.utils.response_utils import create_response
from employees.models import Employee
from attendance.models import Attendance
from django.utils import timezone
from django.shortcuts import get_object_or_404

class CheckInView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    @handle_exceptions
    def post(self, request, employee_id):
        employee = get_object_or_404(Employee, employee_id=employee_id)

        attendance, created = Attendance.objects.get_or_create(
            employee=employee,
            check_in_time = timezone.now(),
            check_out_time__isnull=True,  # Ensure there's no active checkout
        )
        attendance.save()

        return create_response(
            data={'check_in_time': attendance.check_in_time},
            message="Checked in successfully.",
            status_code=status.HTTP_200_OK
        )
