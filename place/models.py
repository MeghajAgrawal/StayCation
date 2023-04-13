from django.db import models
from django.contrib.auth.models import User
from home.models import Destination
from django.urls import reverse
from datetime import datetime, date
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=100)
    address = models.TextField()
    img  = models.ImageField(upload_to='places')
    price= models.IntegerField(default=0)
    rooms= models.IntegerField(default=0)
    max_occupancy=models.IntegerField(default=0)
    offer= models.BooleanField(default=False)
    des_city=models.ForeignKey(Destination,on_delete=models.CASCADE)
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE)
    place_available=models.BooleanField(default=True)
    avg_rate=models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('place-detail',kwargs={'pk':self.pk})
    
    def avg_rating(self):
        sum=0
        ratings=Review.objects.filter(place_review=self)
        if ratings.count>0:
            print(ratings.count)
            for rating in ratings:
                sum=sum+rating.stars
            self.avg_rate=sum/ratings.count
        return self.avg_rate

class Booking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    checkin=models.DateField(auto_now_add=False,auto_now=False,blank=True,default=date.today)
    checkout=models.DateField(auto_now_add=False,auto_now=False,blank=True,default=date.today)
    place=models.ForeignKey(Place,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.user.first_name
    def get_absolute_url(self):
        return reverse('booking-detail',kwargs={'pk':self.pk})

class Review(models.Model):
    user_review=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_review')
    place_review=models.ForeignKey(Place,on_delete=models.CASCADE,related_name='place_review')
    title_review=models.CharField(max_length=100)
    stars=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    content=models.TextField()

    def __str__(self):
        return self.title_review

    def get_absolute_url(self):
        return reverse('review-detail',kwargs={'pk':self.pk})