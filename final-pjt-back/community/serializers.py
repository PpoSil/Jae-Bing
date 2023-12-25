from rest_framework import serializers
from .models import Post, PostComment
from django.contrib.auth import get_user_model


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'content', 'post_code', 'created_at', 'updated_at')


class PostUserSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer()

    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'content', 'post_code', 'created_at', 'updated_at')


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = ('id', 'user', 'post', 'content', 'created_at', 'updated_at')


class PostCommentUserSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer()
    post = PostSerializer()

    class Meta:
        model = PostComment
        fields = ('id', 'user', 'post', 'content', 'created_at', 'updated_at')
