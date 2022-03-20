from django.db import models

from auth_weather.models import WeatherUser
# Create your models here.


class City(models.Model):
    
    name = models.CharField(max_length=255 ,primary_key=True)
    state = models.CharField(max_length=255, blank=True)
    country_code = models.CharField(max_length=255)
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return self.name
    
    class Meta:
        
        db_table = 'city'
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Weather(models.Model):

    city_name = models.ForeignKey(City, on_delete=models.CASCADE)
    temp = models.FloatField()
    feels_like = models.FloatField()
    datetime = models.DateTimeField()
    owner = models.ForeignKey(WeatherUser, verbose_name='Пользователь', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.city_name.name} {self.datetime.isoformat()}"

    class Meta:
        
        db_table = 'weather'
        verbose_name = 'Погода'
        verbose_name_plural = 'Погода'

