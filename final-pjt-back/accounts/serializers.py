from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    followers_count = serializers.SerializerMethodField()

    def get_followers_count(self, obj):
        return obj.followers_count

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'date_of_birth', 'is_superuser', 'date_joined', 'last_login', 'followers_count')
