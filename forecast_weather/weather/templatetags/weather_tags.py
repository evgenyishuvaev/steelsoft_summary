from django import template

from weather.models import Weather, City


register = template.Library()

CITY_LIST = ("Moscow", "Vladivostok", "Stavropol’")


@register.simple_tag(name='forecast_weather')
def get_weather_for_all_cities(user):
    wther = Weather.objects.all()
    user_id = user.id

    msc = wther.filter(city_name=CITY_LIST[0], owner=user_id).order_by("-datetime")[:5].values()
    vld = wther.filter(city_name=CITY_LIST[1], owner=user_id).order_by("-datetime")[:5].values()
    stv = wther.filter(city_name=CITY_LIST[2], owner=user_id).order_by("-datetime")[:5].values()

    return {"msc": msc, "vld": vld, "stv": stv}