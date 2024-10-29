from django.contrib import admin
from attendance.models import Attendance
from employees.models import Employee
from authentication.models import User


admin.site.register(Attendance)
admin.site.register(Employee)
admin.site.register(User)
