from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets


from .models import Booking,Menu
from .serializers import bookingSerializer,menuSerializer

# Create your views here.


class bookingview(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        items = Booking.objects.all()
        serializer = bookingSerializer(items, many=True)
        return Response(serializer.data) # Return JSON
    
    def post(self,request):
        serializer = bookingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data})
        

class menuview(APIView):
    permission_classes = [AllowAny]
    def get(request,self):
        items = Menu.objects.all()
        serializer = menuSerializer(items,many=True)
        return Response(serializer.data) # Return JSON

    def post(self,request):
        serializer = menuSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data})
        

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
    permission_classes = [AllowAny]