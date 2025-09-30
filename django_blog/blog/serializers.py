from rest_framework import serializers
from models import title, content,published_date,author, user, bio, avatar

class postserializer(serializers.ModelSerializer):
    class meta:
        model=MyModel
        fileds=[id,title, content, published_date, author]
        
class ProfileSerializer(serializers.ModelSerializer):
    class meta:
        model=MyModel
        fields=[id, user, bio, avatar]