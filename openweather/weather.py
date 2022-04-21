import datetime

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from flask import jsonify

from openweather.utility.Logger import Logger


class Weather:
    """OpenWeather API implementation class"""

    def __init__(self, api_key, lat, lon, exclude=None):
        """
        Takes the following properties to initiate any request

        :param api_key: This key will be provided by openweather to initiate a request successfully.
        :param lat: The latitude for the location you want to get the weather details
        :param lon: The longitude for the location
        :param exclude: The response details you want the API to ignore
        """
        self.base_url = "https://api.openweathermap.org/data/2.5/onecall"
        self.api_key = api_key
        self.lat = lat
        self.lon = lon
        self.exclude = exclude
        self.logger = Logger()
        self.operation_successful = "Operation Successful"
        self.operation_failed = "Operation Failed"

    def get_current_and_forecast_weather_data(self):
        """
        This method is used to get the weather details for a location

        :return: Dict
        """
        try:
            self.logger.report("DEBUG", datetime.datetime.now(), "Initiating request to get current and forecast weather data")
            if self.exclude:
                params = {"lat": self.lat, "lon": self.lon, "exclude": self.exclude, "appid": self.api_key}
            else:
                params = {"lat": self.lat, "lon": self.lon, "appid": self.api_key}

            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            response = requests.get(self.base_url, params=params, verify=False)
            status_code = response.status_code

            if status_code == 200:
                self.logger.report("INFO", datetime.datetime.now(), "Weather API response: {}".format(response.json()))
                return {"code": "00", "msg": self.operation_successful, "data": response.json()}
            else:
                self.logger.report("ERROR", datetime.datetime.now(), "Failed to process request")
                return {"code": "02", "msg": self.operation_failed, "data": response.json()}

        except Exception as exp:
            self.logger.report("ERROR", datetime.datetime.now(), "Failed to process request: {}".format(str(exp)))
            return jsonify({"code": "02", "msg": self.operation_failed})

