from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from io import BytesIO
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.utils import timezone
from django.db.models import Q
from django.http import FileResponse

from attendance.models import Attendance
from base.utils.response_utils import create_response
from employees.models import Employee

class GenerateDailyAttendanceReportView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        # Get the date parameter (default to today's date)
        date_str = request.query_params.get('date', timezone.now().date().isoformat())
        report_date = timezone.datetime.fromisoformat(date_str)

        # Fetch all attendance records for the given date
        attendances = Attendance.objects.filter(
            check_in_time__date=report_date
        ).select_related('employee')

        if not attendances.exists():
            return create_response(
                data=None,
                message="No attendance records found for the specified date.",
                status_code=404
            )

        # PDF Setup
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        p.setFont("Times-Roman", 8)  # Using a built-in font that should be available

        # Title
        p.drawString(100, 750, f"Daily Attendance Report - {report_date.date()}")
        y = 730

        # Table Header
        headers = ["Employee Name", "Employee ID", "Check-in", "Check-out", "Hours Worked"]
        x_positions = [50, 200, 300, 400, 500]  # Adjusted x positions to fit content

        # Draw header row
        p.setFillColor(colors.black)
        for x, header in zip(x_positions, headers):
            p.drawString(x, y, header)
        y -= 15  # Move down for data rows

        # Draw attendance records for each employee
        for attendance in attendances:
            # Truncate names to fit within column width
            name = (attendance.employee.name[:15] + '...') if len(attendance.employee.name) > 15 else attendance.employee.name
            employee_id = attendance.employee.employee_id
            check_in = attendance.check_in_time.strftime("%H:%M:%S")
            check_out = attendance.check_out_time.strftime("%H:%M:%S") if attendance.check_out_time else "N/A"
            hours_worked = f"{attendance.hours_worked:.2f}"

            # Draw each column value in a row
            row_data = [name, employee_id, check_in, check_out, hours_worked]
            for x, data in zip(x_positions, row_data):
                p.drawString(x, y, data)
            
            y -= 12  # Move down for the next row

            # Handle page breaks
            if y < 50:
                p.showPage()
                p.setFont("Times-Roman", 8)
                y = 750  # Reset y position for new page

        p.showPage()
        p.save()
        buffer.seek(0)

        return FileResponse(buffer, as_attachment=True, filename=f'daily_attendance_report_{report_date.date()}.pdf')
