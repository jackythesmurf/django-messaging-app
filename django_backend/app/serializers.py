from rest_framework import serializers
from .models import User, Messages

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ['username_1', 'username_2', 'content', 'created_at']