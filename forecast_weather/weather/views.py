from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


from rest_framework import generics, permissions

from weather.models import Weather, City
from weather.services.open_weather import get_weather

from weather.serializers import WeatherSerializer
from weather.permissions import IsOwnerOrAdmin, IsForecasterOrAdminElseReadOnly
from weather.forms import LoginUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'weather/login.html'

    def get_success_url(self):
        return reverse_lazy('main_page')


def forecast_logout(request):
    logout(request)
    return redirect('forecast_login')


@login_required(login_url='/')
def forecast_page(request):
    return render(request, 'weather/forecast.html')

@login_required(login_url='/')
def get_forecast_weather(request, city_name):
    
    city = City.objects.get(name=city_name)
    resp_weather = get_weather(city.lat, city.lon)
    resp_weather["city_name"] = city
    resp_weather["owner"] = request.user

    Weather.objects.create(**resp_weather).save()
    return redirect("main_page")


# REST API CRUD for Weather model

class WeatherAPIListCreate(generics.ListCreateAPIView):

    '''
        GET - return Weather list
        POST - return created record, if user is Forecaster or Staff, else return permission denied
    '''

    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    permission_classes = (IsForecasterOrAdminElseReadOnly, )

    def get_queryset(self):
        queryset = Weather.objects.all()
        city_name = self.request.query_params.get('city_name')

        if city_name is not None:
            queryset = queryset.filter(city_name=city_name)
        
        return queryset


class WeatherAPIUpdate(generics.UpdateAPIView):

    '''
        PUT - provide update chosen record, if  user owner or Staff, else return permission denied
        PATCH - provide update choosen fields, if  user owner or Staff, else return permission denied
    '''

    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    permission_classes = (IsOwnerOrAdmin, )


class WeatherAPIRetrieve(generics.RetrieveAPIView):

    '''
        GET - return choosen record by <int:pk>
    '''

    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    permission_classes = (permissions.AllowAny, )
    


class WeatherAPIDelete(generics.DestroyAPIView):
    
    '''
        DELETE - delete choosen record by <int:pk>, if  user owner or Staff, else return permission denied
    '''

    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    permission_classes = (IsOwnerOrAdmin, )
