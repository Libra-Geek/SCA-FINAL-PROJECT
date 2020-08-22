from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png',blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:50] + '...Read More'
    # add in thumbnail later
    # add in Author later
# everytime we make a model or make a change to a model, we execute the commands:
# python manage.py makemigrations
# python manage.py migrate
# The ORM is the gap between the code and the database and it is built into Django
# We can save, update or retrieve a model using the ORM
