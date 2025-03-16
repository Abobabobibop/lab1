# chat_project/views.py

from rest_framework.views import APIView
from rest_framework.response import Response

class AboutView(APIView):
    """
    Returns static information about the app.
    """
    def get(self, request, format=None):
        data = {
            "emblem": "https://example.com/static/emblem.png",  # Replace with your emblem URL or static file path.
            "description": "This is a simple chat application developed using Django and Django REST Framework."
        }
        return Response(data)
