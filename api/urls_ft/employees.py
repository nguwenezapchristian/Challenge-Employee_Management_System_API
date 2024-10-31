from django.urls import path
from api.views.employees.create import CreateEmployeeView
from api.views.employees.retrieve import RetrieveEmployeeView, ListEmployeesView
from api.views.employees.update import UpdateEmployeeView
from api.views.employees.delete import DeleteEmployeeView

app_name = 'employees'

urlpatterns = [
    # List and Create
    path('', ListEmployeesView.as_view(), name='employee-list'),
    path('create/', CreateEmployeeView.as_view(), name='employee-create'),
    
    # Retrieve, Update, Delete
    path('<str:employee_id>/', RetrieveEmployeeView.as_view(), name='employee-detail'),
    path('<str:employee_id>/update/', UpdateEmployeeView.as_view(), name='employee-update'),
    path('<str:employee_id>/delete/', DeleteEmployeeView.as_view(), name='employee-delete'),
    
    # Search, WORK ON IT LATER
    # path('search/', ListEmployeesView.as_view(), name='employee-search'),
]