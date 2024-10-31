from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.utils import timezone
from django.db.models import Q
from django.http import HttpResponse
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
from io import BytesIO

from attendance.models import Attendance
from base.utils.response_utils import create_response
from employees.models import Employee

class GenerateDailyExcelReportView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        # Get the date parameter (default to today's date)
        date_str = request.query_params.get('date', timezone.now().date().isoformat())
        report_date = timezone.datetime.fromisoformat(date_str).date()

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

        # Create a new Excel workbook and sheet
        wb = Workbook()
        ws = wb.active
        ws.title = "Attendance Report"

        # Set up header
        headers = ["Employee Name", "Employee ID", "Date", "Check-in", "Check-out", "Hours Worked"]
        ws.append(headers)
        
        # Style the header row
        header_font = Font(bold=True)
        for cell in ws[1]:
            cell.font = header_font
            cell.alignment = Alignment(horizontal="center")

        # Populate the Excel sheet with attendance data
        for attendance in attendances:
            employee_name = attendance.employee.name
            employee_id = attendance.employee.employee_id
            date = attendance.check_in_time.date()
            check_in_time = attendance.check_in_time.strftime("%H:%M:%S")
            check_out_time = attendance.check_out_time.strftime("%H:%M:%S") if attendance.check_out_time else "N/A"
            hours_worked = f"{attendance.hours_worked:.2f}" if attendance.hours_worked else "N/A"
            
            ws.append([employee_name, employee_id, date, check_in_time, check_out_time, hours_worked])

        # Adjust column widths
        for column_cells in ws.columns:
            length = max(len(str(cell.value)) for cell in column_cells)
            ws.column_dimensions[column_cells[0].column_letter].width = length + 2

        # Save the workbook to a BytesIO stream
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename=daily_attendance_report_{report_date}.xlsx'

        with BytesIO() as buffer:
            wb.save(buffer)
            response.write(buffer.getvalue())

        return response
