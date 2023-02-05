"""
Views for the user API.
"""

from rest_framework import generics
from serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    """Create a new suer in the syste."""
    serializer_class = UserSerializer