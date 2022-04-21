**OPEN WEATHER LIBRARY (UNOFFICIAL)**

The library is used to get the current and forecast weather data from open-weather.

**Below describes how the library can be used:**
1. Create an account on https://openweathermap.org/ to get your api_key.
2. Download and build the library using the command: python3 setup.py bdist_wheel
3. Install the library using the command: pip install py-open-weather-lib/dist/openweather-0.1.0-py3-none-any.whl
4. Import the Weather class: from openweather.weather import Weather
5. Create an instance of the Weather class and pass your api_key, lat and lon to the constructor: 
   Example: weather = Weather(api_key="a25fd6....", lat=5.614818, lon=-0.205874)
6. Call the method to return the weather data: weather.get_current_and_forecast_weather_data()
7. That's it. The method will return an object contain all the weather data

**VERY IMPORTANT**: 
1. For successful requests the response structure is {"code": "00", "msg": "Operation Successful", "data": {}}
The data object contains the weather details. Click https://openweathermap.org/api/one-call-api to 
see a sample response
2. For failed requests the response structure is {"code": "02", "msg": "Operation Failed"}
   