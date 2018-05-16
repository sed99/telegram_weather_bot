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
        self.key = key  # Your Secret Key

    def get_data(self, latitude=None, longitude=None, **options):
        """
        Method for requesting data from the site.
        Метод для запроса данных с сайта.
        """
        try:
            if not isinstance(latitude, float):
                raise InputError("<class 'float'>, don't %s" % (type(latitude)))
            if not isinstance(longitude, float):
                raise InputError("<class 'float'>, don't %s" % (type(longitude)))

            url_str = "https://api.darksky.net/forecast"
            coord = "%f,%f" % (latitude, longitude)
            key = self.key
            answer = requests.get("%s/%s/%s" % (url_str, key, coord), params=options, timeout=3)
            return answer.json()
        except WeatherError as e:
            raise e

