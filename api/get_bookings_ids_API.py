from api.api_call import ApiCall
from config.config import URL


class GetBookingIdsAPI(ApiCall):
    """Return the ids of all the bookings that exist within the API.
    Can take optional query strings to search and return a subset of booking ids."""
    path = URL.BOOKING_ROUTE

    def __init__(self, headers=None, query_params=None,  **kwargs):
        super().__init__(method='get', headers=headers, query_params=query_params, **kwargs)
