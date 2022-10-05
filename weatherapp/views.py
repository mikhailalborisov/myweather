import requests
from django.shortcuts import render

from myweather.settings import OWM_CITY, OWM_API_KEY


# Create your views here.

def index(request):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={OWM_CITY}&appid={OWM_API_KEY}")
    prin = response.json()
    return render(request, "index.html", context={
        "OWM_CITY": OWM_CITY,
        "temp": round(prin['main']['temp'] - 273, 2)
    })
