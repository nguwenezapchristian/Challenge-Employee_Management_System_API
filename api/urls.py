from django.urls import path, include

urlpatterns = [
    path('employees/', include('api.urls_ft.employees')),
    path('attendance/', include('api.urls_ft.attendance')),
    path('auth/', include('api.urls_ft.authentication')),
]