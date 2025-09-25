from rest_framework import serializers
from .models import MyModel
from models import name
from BookSerializer import BookSerializer

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = MyModel
        fields = [id, name]