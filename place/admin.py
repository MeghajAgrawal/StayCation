from django.contrib import admin
from .models import Place,Booking,Review
# Register your models here.
admin.site.register(Place)
admin.site.register(Booking)
admin.site.register(Review)