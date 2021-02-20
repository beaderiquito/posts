from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50] #displays the first 50 characters of text field