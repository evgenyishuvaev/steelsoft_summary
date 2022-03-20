from email.policy import default
from rest_framework import serializers

from weather.models import Weather

class WeatherSerializer(serializers.ModelSerializer):
    
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Weather
        fields = '__all__'

