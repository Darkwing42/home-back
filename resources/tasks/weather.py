from home_back.models.weather import City, WeatherConfig, WeatherData
import requests

WEATHER_URL_BASE = 'https://api.opentweathermap.org/data/2.5/weather?q=' 

def getCurrentWeather(city_name, countryCode):
    config = WeatherConfig.get_config()
    api_key = config.api_key

    city = City.query.filter_by(city_name=city_name).first()
    r = requests.get(WEATHER_URL_BASE + City  + countryCode + ',&appid=' + api_key + '&units=metric')
    
    
    
