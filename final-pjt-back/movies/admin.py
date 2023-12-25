from django.contrib import admin
from .models import Genre, Movie, Review, UserGenre

# Register your models here.
admin.site.register(Genre)
admin.site.register(UserGenre)
admin.site.register(Movie)
admin.site.register(Review)
