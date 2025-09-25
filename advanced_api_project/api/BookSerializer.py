from rest_framework import serializers
from .models import MyModel
from models import title
from models import publication_year
import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = [id, title, publication_year]

    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
    

    # AuthorSerializer nests BookSerializer under `books`, so whenever an Author
# is serialized, their books will appear inline.
# Example:
# {
#   "id": 1,
#   "name": "George Orwell",
#   "books": [
#       {"id": 1, "title": "1984", "publication_year": 1949, "author": 1},
#       {"id": 2, "title": "Animal Farm", "publication_year": 1945, "author": 1}
#   ]
# }
