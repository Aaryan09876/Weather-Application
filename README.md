# WEATHER-APPLICATION
Weather App is a Python-based tool that fetches real-time weather data for any city using the OpenWeatherMap API.
It displays current temperature, humidity, wind speed, pressure, and weather conditions in a clean, readable format. 
The project demonstrates API integration, JSON parsing, and error handling while keeping the code beginner-friendly and well-structured.


#KEY FEATURE

1.Live Weather Data*: Get current temperature in °C/°F, humidity, wind speed, and conditions for any city worldwide
2.Error Handling*: Gracefully manages invalid city names, network failures, missing API keys, and rate limits


#TECHNICAL DETAILS

1.When you enter a city name, the app sends a GET request to OpenWeatherMap's Current Weather endpoint.
2.If the response status is 200, it parses the JSON to extract temp, humidity, wind.speed, and weather.description.
3.All exceptions like ConnectionError, Timeout, and HTTPError are caught and returned as user-friendly messages instead of crashes.


#IMPORTANT NOTES

1.Weather data accuracy depends on OpenWeatherMap. The free tier allows 60 API calls/minute and 1M calls/month.
2.Data refreshes every ~10 minutes server-side. This project is for educational/personal use only.
3.Do not use it as the sole source for weather-critical decisions.
