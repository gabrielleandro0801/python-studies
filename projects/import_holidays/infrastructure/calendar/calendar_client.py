import requests


class CalendarClient:

    def __init__(self):
        self._token = ''

    def list(self, params: dict):
        params["token"] = self._token
        response = requests.get(url='', params=params)
        return response.json()
