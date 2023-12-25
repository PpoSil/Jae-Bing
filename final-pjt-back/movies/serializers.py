from rest_framework import serializers
from .models import Movie, Genre, Review
from django.contrib.auth import get_user_model

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')


class GenreSerializer(serializers.ModelSerializer):
    class Meta :
        model = Genre
        fields = ('id', 'name')

class MovieSerializer(serializers.ModelSerializer):
    genre_ids = GenreSerializer(many=True)
    class Meta:
        model = Movie
        fields = ('id','movie_no','title','genre_ids','admin_reg','vote_average','vote_count','release_date','adult','overview','poster_path', 'backdrop_path')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id','user','movie','content','rate','like','created_at','updated_at')


class ReviewUserSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer()
    movie = MovieSerializer()
    class Meta:
        model = Review
        fields = ('id','user','movie','content','rate','like','created_at','updated_at')