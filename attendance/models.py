from django.db import models
from base.models import BaseModel

class Attendance(BaseModel):
    employee = models.ForeignKey(
        'employees.Employee',
        on_delete=models.CASCADE,
        related_name='attendances'
    )
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'attendances'

    @property
    def hours_worked(self):
        if self.check_out_time and self.check_in_time:
            duration = self.check_out_time - self.check_in_time
            return round(duration.total_seconds() / 3600, 2)
        return 0
