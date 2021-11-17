from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.title.capitalize()
