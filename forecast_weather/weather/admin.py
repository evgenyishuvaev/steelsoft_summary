from django.contrib import admin

from weather.models import Weather, City


admin.site.register(Weather)
admin.site.register(City)