import requests
import json

apikey = "474d59dd890c4108f62f192e0c6fce01"
cities = ["Tokyo, JP", "London, UK", "New York, US"]
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"
k2c = lambda k: k - 273.15
for name in cities:
    url = api.format(city=name, key = apikey)
    r = requests.get(url)
    data = json.loads(r.text)
    print(" + 都市=", data["name"])
    print(" | 天気=", data["weather"][0]["description"])
    print(" | 最低温気=", k2c(data["main"]["temp_min"]))
    print(" | 最高温気=", k2c(data["main"]["temp_max"]))
    print(" | 湿度=", data["main"]["humidity"])
    print(" | 気圧=", data["main"]["pressure"])
    print(" | 風向き=", data["wind"]["deg"])
    print(" | 風速度=", data["wind"]["speed"])
    print("")

