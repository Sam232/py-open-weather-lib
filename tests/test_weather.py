from openweather.weather import Weather


def test_get_current_and_forecast_weather_data():
    weather = Weather(api_key="a297ae5fd6dd655918a8c78da676e506", lat=5.614818, lon=-0.205874)
    weather.get_current_and_forecast_weather_data()

    weather_api_response = Weather(api_key="a297ae5fd6dd655918a8c78da676e506", lat=5.614818, lon=-0.205874)\
        .get_current_and_forecast_weather_data()
    assert weather_api_response.get("code") == "00"

