from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from auth_weather.models import WeatherUser
# Register your models here.


class AuthWeatherAdmin(UserAdmin):
    model = WeatherUser
    fieldsets = *UserAdmin.fieldsets, ("Role", {"fields": ("is_forecaster", )}),


admin.site.register(WeatherUser, AuthWeatherAdmin)