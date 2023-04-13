from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from place.models import Place

# Create your models here.
class Feedback(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content=models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('fb-detail',kwargs={'pk':self.pk})
    
