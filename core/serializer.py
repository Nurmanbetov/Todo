from django.contrib.auth.models import User 
from rest_framework import serializers

class UserSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "url", "username", "email", "first_name", 
            "last_name","is_staff"
        ]