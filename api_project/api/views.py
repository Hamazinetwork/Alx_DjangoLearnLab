from django.shortcuts import render
from rest_framework import generics
from .models import MyModel
from .serializers import MyModelSerializer

# Create your views here.
class BookList(generics.ListCreateAPIView):
    queryset = MyModel.object.all()
    serializer_class = MyModelSerializer