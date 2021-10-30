from typing import List

import requests


class CalendarClient:

    def __init__(self, url: str, token: str):
        self._url: str = url
        self._token: str = token

    def list(self, params: dict) -> List[dict]:
        params["token"] = self._token
        response = requests.get(url=self._url, params=params)
        return response.json()
