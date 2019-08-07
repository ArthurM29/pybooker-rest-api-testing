import urllib.parse
import requests
import json
from config.config import URL


class ApiCall:
    base_url = URL.BASE_URL
    path = ''

    def __init__(self, method, headers=None, payload=None, query_params=None, **kwargs):
        self.url = urllib.parse.urljoin(self.base_url, self.path)
        self.method = method
        self.headers = headers
        self.payload = payload
        self.query_params = query_params
        self.kwargs = kwargs

    def call(self):
        if self.method:
            print(
                f"Calling route: {self.url}, method: {self.method.upper()}, payload = {self.payload}, "
                f"headers = {self.headers}, query_params = {self.query_params}, **kwargs = {self.kwargs}")

            response = requests.request(self.method, self.url, data=self.payload, headers=self.headers,
                                        params=self.query_params)
            print(f"Response: Status code: {response.status_code}, Body: {json.dumps(response.text, indent=2)}")
            return response
        else:
            raise Exception('Invalid verb')
