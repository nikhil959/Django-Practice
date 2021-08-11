from rest_framework import serializers
from .models import Users


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'full_name', 'email_id', 'phone_number', 'password']
