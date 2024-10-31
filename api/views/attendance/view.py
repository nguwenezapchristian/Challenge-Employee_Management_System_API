from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from base.utils.decorators import handle_exceptions
from base.utils.response_utils import create_response
from attendance.models import Attendance
from django.shortcuts import get_object_or_404
from employees.models import Employee

class ViewAttendanceView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    @handle_exceptions
    def get(self, request, employee_id):
        employee = get_object_or_404(Employee, employee_id=employee_id)
        attendances = Attendance.objects.filter(employee=employee)

        # Optional filtering by date range
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if start_date and end_date:
            attendances = attendances.filter(check_in_time__date__range=[start_date, end_date])

        data = [
            {
                'check_in_time': attendance.check_in_time,
                'check_out_time': attendance.check_out_time,
                'hours_worked': attendance.hours_worked
            }
            for attendance in attendances
        ]

        return create_response(
            data=data,
            message="Attendance records retrieved successfully.",
            status_code=status.HTTP_200_OK
        )