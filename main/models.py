from django.db import models


class User(models.Model):
    """User model class is here."""
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=50)
