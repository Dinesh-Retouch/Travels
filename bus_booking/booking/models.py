from django.db import models
from django.contrib.auth.models import User

class Bus(models.Model):
    name = models.CharField(max_length=100)
    route = models.CharField(max_length=100)
    timing = models.CharField(max_length=100)
    available_seats = models.PositiveIntegerField()
    seats_layout = models.CharField(max_length=10, default='2x2')
    total_seats = models.PositiveIntegerField(default=40)
    tracking_link = models.URLField(blank=True, null=True)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    cancelled = models.BooleanField(default=False)

# Make sure this Review model exists here:
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
