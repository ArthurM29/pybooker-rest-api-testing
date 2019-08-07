from api.api_call import ApiCall
from config.config import URL


class AuthenticateAPI(ApiCall):
    """Creates a new auth token to use for access to the PUT and DELETE /booking"""
    path = URL.AUTHENTICATE_ROUTE

    def __init__(self, headers=None, payload=None, **kwargs):
        if headers is None:
            self.headers = {'content-type': 'application/json'}
        else:
            self.headers = headers
        super().__init__(method='post', headers=self.headers, payload=payload, **kwargs)
