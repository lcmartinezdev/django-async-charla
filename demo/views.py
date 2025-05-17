import requests
import httpx
from django.http import JsonResponse

from .utils import get_weather_url

london_url = get_weather_url("London")
tokyo_url = get_weather_url("Tokyo")
pittsburgh_url = get_weather_url("Pittsburgh")
equator_url = get_weather_url("Ecuador")
chile_url = get_weather_url("Chile")
colombia_url = get_weather_url("Colombia")


def sync_weather_view(request):
    london_res = requests.get(london_url)
    tokyo_res = requests.get(tokyo_url)
    pittsburgh_res = requests.get(pittsburgh_url)
    equator_res = requests.get(equator_url)
    chile_res = requests.get(chile_url)
    colombia_res = requests.get(colombia_url)

    return JsonResponse(
        {
            "london": london_res.json(),
            "tokyo": tokyo_res.json(),
            "pittsburgh": pittsburgh_res.json(),
            "equator": equator_res.json(),
            "chile": chile_res.json(),
            "colombia": colombia_res.json(),
        }
    )


async def async_weather_view(request):
    async with httpx.AsyncClient() as client:
        london_res = await client.get(london_url)
        tokyo_res = await client.get(tokyo_url)
        pittsburgh_res = await client.get(pittsburgh_url)
        equator_res = await client.get(equator_url)
        chile_res = await client.get(chile_url)
        colombia_res = await client.get(colombia_url)

    return JsonResponse(
        {
            "london": london_res.json(),
            "tokyo": tokyo_res.json(),
            "pittsburgh": pittsburgh_res.json(),
            "equator": equator_res.json(),
            "chile": chile_res.json(),
            "colombia": colombia_res.json(),
        }
    )
