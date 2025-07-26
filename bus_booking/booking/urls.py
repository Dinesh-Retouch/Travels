from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search_buses, name='search_buses'),
    path('book/<int:bus_id>/', views.book_bus, name='book_bus'),
    path('track/<int:bus_id>/', views.track_bus, name='track_bus'),
    path('book/<int:bus_id>/', views.book_seat, name='book_seat'),
    path('track/<int:bus_id>/', views.bus_tracking, name='bus_tracking'),
]
