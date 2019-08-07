from api.api_call import ApiCall
from config.config import URL


class GetBookingAPI(ApiCall):
    """Returns a specific booking based upon the booking id provided"""
    path = URL.BOOKING_ID_ROUTE

    def __init__(self, booking_id, headers=None, query_params=None, **kwargs):
        if headers is None:
            self.headers = {'accept': 'application/json'}
        else:
            self.headers = headers
        super().__init__(method='get', headers=self.headers, query_params=query_params, **kwargs)
        self.booking_id = booking_id
        self.url = self.url.format(bookingId=booking_id)
