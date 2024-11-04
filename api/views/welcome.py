from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

class WelcomeView(APIView):
    """
    API endpoint for welcome message
    """
    permission_classes = [AllowAny]
    def get(self, request):
        return Response({"Status": "Success",
                         "Message": "Welcome to Employee Management System API!",
                         "Description": "The Employee Management System API is designed to handle essential tasks for managing employees, attendance, and attendance reporting."
                         })