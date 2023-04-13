from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profiles_pics')
    phone_number=models.BigIntegerField(default='00')
    age=models.IntegerField(default='0')
    dob=models.DateField(auto_now_add=False,auto_now=False,blank=True,default=date.today)    
    def save(self,**kwargs):
        super().save()
        img=Image.open(self.image.path)
        if img.height>300 or img.width>300:
            output=(300,300)
            img.thumbnail(output)
            img.save(self.image.path)




