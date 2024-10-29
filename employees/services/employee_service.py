from django.db import models
from django.db.models import Max
import re

class EmployeeService:
    @staticmethod
    def generate_employee_id():
        """
        Generates a unique employee ID in the format EMP001, EMP002, etc.
        """
        from employees.models import Employee

        # Get the last employee ID
        last_employee = Employee.objects.all().aggregate(
            Max('employee_id')
        )['employee_id__max']

        if not last_employee:
            # If no employees exist, start with EMP001
            return 'EMP001'

        # Extract the number from the last employee ID
        last_number = int(re.findall(r'\d+', last_employee)[0])
        
        # Generate new employee ID with incremented number
        new_number = last_number + 1
        return f'EMP{new_number:03d}'

    @staticmethod
    def validate_employee_id(employee_id):
        """
        Validates if the employee ID matches the required format
        """
        if not re.match(r'^EMP\d{3}$', employee_id):
            raise ValueError(
                'Employee ID must be in the format EMP followed by 3 digits (e.g., EMP001)'
            )
        return True