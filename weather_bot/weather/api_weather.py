# -*- coding: utf8 -*-
__author__ = "D. Belavin"


import requests

from weather_bot.weather.WeatherErorrs import *


class Weather(object):
    """
    Base class for working with the api site: DarkSky.net
    Базовый класс для работы с api сайта: DarkSky.net
    """

    def __init__(self, key):
        if not isinstance(key, str):
            e = f"The key must be of type: <class 'string'>. You key = {type(key)}"
            raise SecretKeyError(e)

        self.key = key  # Your Secret Key

    def get_data(self, latitude=None, longitude=None, options=None):
        """
        Method for requesting data from the site.
        Метод для запроса данных с сайта.
        """
        try:
            if not isinstance(latitude, float):
                e = f"latitude = <class 'float'>. You latitude = {type(latitude)}"
                raise InputError(e)
            if not isinstance(longitude, float):
                e = f"longitude = <class 'float'>, You longitude = {type(longitude)}"
                raise InputError(e)

            url_str = "https://api.darksky.net/forecast"
            coord = "%f,%f" % (latitude, longitude)
            key = self.key
            answer = requests.get("%s/%s/%s" % (url_str, key, coord), params=options, timeout=3)
            if answer.status_code is 200:
                return answer.json()
            else:
                return answer.status_code
        except WeatherError as e:
            raise e

