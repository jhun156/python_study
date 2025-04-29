# movies/models.py

from django.db import models
from django.conf import settings

class Hashtag(models.Model):
    content = models.TextField(unique=True)

    def __str__(self):
        return self.content

class Movie(models.Model):
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
                             
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, 
                                                     related_name='like_movies')                         
    title = models.CharField(max_length=20)
    description = models.TextField()


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
