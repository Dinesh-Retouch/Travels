from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Bus, Booking
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.db import IntegrityError

def home(request):
    buses = Bus.objects.all()
    return render(request, 'booking/home.html', {'buses': buses})

def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        
        # Check if fields are empty
        if not username or not password:
            return render(request, 'booking/registration.html', {
                'error': 'All fields are required.'
            })

        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('login')  # Or home page
        except IntegrityError:
            return render(request, 'booking/registration.html', {
                'error': 'Username already exists. Please choose another.'
            })

    return render(request, 'booking/registration.html')

def login_view(request):
    # Login logic
    return render(request, 'booking/login.html' ,{'error':'login sucessfull'} )

def logout_view(request):
    logout(request)
    return redirect('home')

def profile(request):
    user_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/profile.html', {'bookings': user_bookings})

    # Bus search logic
    pass

def book_seat(request, bus_id):
    # Seat booking logic
    return render(request, 'booking/book.html', {'bus_id': bus_id})

def bus_tracking(request, bus_id):
    bus = Bus.objects.get(id=bus_id)
    return render(request, 'booking/tracking.html', {'bus': bus})



def book_bus(request, bus_id):
    # Add logic to handle booking
    return render(request, 'booking/book.html', {'bus_id': bus_id})

def track_bus(request, bus_id):
    # Add logic to handle tracking
    return render(request, 'booking/track.html', {'bus_id': bus_id})

def search_buses(request):
    return HttpResponse("Search buses view")