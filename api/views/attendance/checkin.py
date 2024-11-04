from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from base.utils.decorators import handle_exceptions
from base.utils.response_utils import create_response
from employees.models import Employee
from attendance.models import Attendance
from django.utils import timezone
from django.shortcuts import get_object_or_404
from base.utils.tasks import send_email_task

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

        # Send email notification to the employee
        subject = "Attendance Check-In"
        text_body = f"Hi {employee.name},\n\nYou've checked in at {timezone.now().strftime('%Y-%m-%d %H:%M:%S')}.\n\nPlease make sure to check out before 12:00 PM."
        html_body = f"<p>Hi {employee.name},</p><p>You've checked in at {timezone.now().strftime('%Y-%m-%d %H:%M:%S')}. Please make sure to check out before 12:00 PM.</p>"

        send_email_task.delay(employee.email, subject, text_body, html_body)

        return create_response(
            data={'check_in_time': attendance.check_in_time},
            message="Checked in successfully.",
            status_code=status.HTTP_200_OK
        )
