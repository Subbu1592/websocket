from django.db import models

# Create your models here.


class Message(models.Model):
    username = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    content = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']
