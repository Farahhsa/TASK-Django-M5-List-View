from rest_framework.generics import ListAPIView
from flights.models import Flight, Booking
from .serilaizers import FlightSerializer, BookingSerializer
from django.utils import timezone

class ListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer



class Booking_list(ListAPIView):
    queryset = Booking.objects.filter(date__gt=timezone.now())
    serializer_class = BookingSerializer

