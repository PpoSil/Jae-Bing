from django.db import models
from django.conf import settings

class Genre(models.Model):
  name = models.CharField(max_length=50)

class Movie(models.Model):
  movie_no = models.IntegerField()
  title = models.CharField(max_length=100)
  original_title = models.CharField(max_length=100)
  release_date = models.DateField(null=True)
  poster_path = models.CharField(max_length=200, null=True)
  backdrop_path = models.CharField(max_length=255, null=True)
  adult = models.BooleanField(default=False)
  video = models.BooleanField(default=False)
  original_language = models.CharField(max_length=50)
  overview = models.TextField()
  vote_count = models.IntegerField(default=0)
  vote_average = models.FloatField(default=0.0)
  popularity = models.FloatField(default=0.0)
  genre_ids = models.ManyToManyField(Genre, related_name='movie_genres')
  admin_reg = models.BooleanField(default=False)

class Review(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  content = models.TextField()
  rate = models.IntegerField(default=0)
  like = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class UserGenre(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  action = models.IntegerField(default=0)
  adventure = models.IntegerField(default=0)
  animation = models.IntegerField(default=0)
  comedy = models.IntegerField(default=0)
  crime = models.IntegerField(default=0)
  documentary = models.IntegerField(default=0)
  drama = models.IntegerField(default=0)
  family = models.IntegerField(default=0)
  fantasy = models.IntegerField(default=0)
  history = models.IntegerField(default=0)
  horror = models.IntegerField(default=0)
  music = models.IntegerField(default=0)
  mystery = models.IntegerField(default=0)
  romance = models.IntegerField(default=0)
  science_fiction = models.IntegerField(default=0)
  tv_movie = models.IntegerField(default=0)
  thriller = models.IntegerField(default=0)
  war = models.IntegerField(default=0)
  western = models.IntegerField(default=0)