from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from base.utils.decorators import handle_exceptions
from base.utils.response_utils import create_response
from attendance.models import Attendance
from employees.models import Employee
from django.utils import timezone
from django.shortcuts import get_object_or_404
from base.utils.tasks import send_email_task

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

        # send email notification to employee
        subject = "Attendance Check-Out"
        text_body = f"Hi {employee.name},\n\nYou've checked out at {timezone.now().strftime('%Y-%m-%d %H:%M:%S')}.\n\nYour attendance record has been updated."
        html_body = f"<p>Hi {employee.name},</p><p>You've checked out at {timezone.now().strftime('%Y-%m-%d %H:%M:%S')}. Your attendance record has been updated.</p>"

        send_email_task.delay(employee.email, subject, text_body, html_body)

        return create_response(
            data={'check_out_time': attendance.check_out_time},
            message="Checked out successfully.",
            status_code=status.HTTP_200_OK
        )
