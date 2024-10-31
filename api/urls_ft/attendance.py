from django.urls import path
from api.views.attendance.checkin import CheckInView
from api.views.attendance.checkout import CheckOutView
from api.views.attendance.view import ViewAttendanceView
from api.views.attendance.report_pdf import GenerateDailyAttendanceReportView
from api.views.attendance.excel_report import GenerateDailyExcelReportView

urlpatterns = [
    path('check-in/<str:employee_id>/', CheckInView.as_view(), name='check-in'),
    path('check-out/<str:employee_id>/', CheckOutView.as_view(), name='check-out'),
    path('view/<str:employee_id>/', ViewAttendanceView.as_view(), name='view-attendance'),
    path('report/pdf/', GenerateDailyAttendanceReportView.as_view(), name='generate-pdf-report'),
    path('report/excel/', GenerateDailyExcelReportView.as_view(), name='generate-excel-report'),
]
