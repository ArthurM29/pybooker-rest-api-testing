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
                f"\n---->Request: {self.url}, method: {self.method.upper()} \npayload = {self.payload}, "
                f"\nheaders = {self.headers}, query_params = {self.query_params}, **kwargs = {self.kwargs}")

            response = requests.request(self.method, self.url, data=self.payload, headers=self.headers,
                                        params=self.query_params)
            # TODO handle the case when json() deserialization fails when request fails
            print(f"<----Response: \nStatus code: {response.status_code} \nBody: {json.dumps(response.json(), indent=2)}")
            return response
        else:
            raise Exception('Invalid verb')

