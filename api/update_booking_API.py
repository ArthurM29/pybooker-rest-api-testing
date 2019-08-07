from api.api_call import ApiCall
from config.config import URL


class UpdateBookingAPI(ApiCall):
    """Updates a current booking"""
    path = URL.BOOKING_ID_ROUTE

    def __init__(self, headers=None, payload=None, **kwargs):
        if headers is None:
            self.headers = {'content-type': 'application/json', 'accept': 'application/json'}
        else:
            self.headers = headers
        super().__init__(method='post', headers=self.headers, payload=payload, **kwargs)
