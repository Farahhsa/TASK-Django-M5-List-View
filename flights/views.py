from rest_framework.generics import ListAPIView
from flights.models import Flight, Booking
from .serilaizers import FlightSerializer

class ListView(ListAPIView):
    queryset = Flight.objects.all()    
    serializer_class = FlightSerializer



class Booking_list(ListAPIView):
    class Meta:
        model = Booking
        fields = ['flight', 'date', 'id',]

