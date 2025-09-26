from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Menu
        fields = '__all__'

class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = '__all__'


class userSerializer(serializers.ModelSerializer):
    class meta:
        model = User
        fields = ['url','username','email','gruups']