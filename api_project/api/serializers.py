from rest_framework import serializers
from .models import MyModel
from models import author
from models import title

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = [id, author, title]