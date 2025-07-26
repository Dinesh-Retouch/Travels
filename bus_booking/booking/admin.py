from django.contrib import admin
from .models import Bus, Booking, Review    

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('name', 'route', 'timing', 'available_seats', 'total_seats')

