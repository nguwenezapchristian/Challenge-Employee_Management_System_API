from django.urls import path, include

urlpatterns = [
    path('employees/', include('api.urls_ft.employees')),
]