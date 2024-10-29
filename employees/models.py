from django.db import models
from base.models import BaseModel
from django.core.validators import RegexValidator
from .services.employee_service import EmployeeService

class Employee(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    employee_id = models.CharField(
        max_length=10, 
        unique=True, 
        editable=False
    )
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message='Phone number must be in format: +999999999'
            )
        ]
    )
    user = models.OneToOneField(
        'authentication.User',
        on_delete=models.CASCADE,
        related_name='employee_profile'
    )

    class Meta:
        db_table = 'employees'

    def save(self, *args, **kwargs):
        if not self.employee_id:
            self.employee_id = EmployeeService.generate_employee_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.employee_id})"