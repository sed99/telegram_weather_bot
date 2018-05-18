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
        self.timeout = 1  # timeout for requests

    def get_data(self, latitude, longitude, options):
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
            answer = requests.get("%s/%s/%s" % (url_str, key, coord), params=options, timeout=self.time)
            if answer.status_code is 200:
                return answer.json()
            else:
                return answer.status_code
        except WeatherError as e:
            raise e

    def get_currently(self, latitude, longitude, options=None):  # на данный момент
        if options is None:
            options = dict()
        options["exclude"] = "minutely,hourly,daily,alerts,flags"
        currently = self.get_data(latitude=latitude, longitude=longitude, options=options)
        return currently

    def get_hourly(self, latitude, longitude, options=None):
        """
        The forecast for the day.
        Прогноз на 24 часа с времени запроса.
        """

        if options is None:
            options = dict()
        options["exclude"] = "currently,minutely,daily,alerts,flags"
        hourly = self.get_data(latitude, longitude, options)
        return hourly

    def get_daily(self, latitude, longitude, options=None):
        """
        Weekly forecast.
        Прогноз на одну неделю.
        """

        if options is None:
            options = dict()
        options["exclude"] = "currently,hourly,minutely,alerts,flags"
        daily = self.get_data(latitude, longitude, options)
        return daily
