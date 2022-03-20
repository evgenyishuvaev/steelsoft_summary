from django.urls import path, re_path, include

from weather import views


urlpatterns = [
    path('', views.LoginUser.as_view(), name='forecast_login'),
    path('logout', views.forecast_logout, name='forecast_logout'),
    path('forecast', views.forecast_page, name='main_page'),
    path('forecast/<str:city_name>', views.get_forecast_weather, name='get_weather'),

    # REST API AUTH
    # re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    #REST API CRUD operations
    path('api/v1/weather', views.WeatherAPIListCreate.as_view(), name='api_weather_list_create'),
    path('api/v1/weather/<int:pk>', views.WeatherAPIRetrieve.as_view(), name="api_weather_retrive"), 
    path('api/v1/weather/update/<int:pk>', views.WeatherAPIUpdate.as_view(), name="api_weather_update"), 
    path('api/v1/weather/delete/<int:pk>', views.WeatherAPIDelete.as_view(), name="api_weather_delete"),
]