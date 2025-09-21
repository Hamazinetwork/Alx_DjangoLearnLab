from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import BookSerializer

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.object.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        return [IsAdminUser()]
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



# Authentication & Permissions:
# - TokenAuthentication is enabled globally (settings.py).
# - BookList requires any authenticated user.
# - BookViewSet allows authenticated users to read, but only admins can write.
# Token retrieval: POST /api/auth/token/ with {"username": "", "password": ""}.
