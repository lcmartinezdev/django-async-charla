from django.conf import settings

def get_weather_url(city):
    api_key = settings.DJANGO_WEATHER_API_KEY
    base_url = "https://api.weatherapi.com/v1/current.json"
    return f"{base_url}?key={api_key}&q={city}"
