from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Status(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        null=True, default=None
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', args=[self.id])
    



    

