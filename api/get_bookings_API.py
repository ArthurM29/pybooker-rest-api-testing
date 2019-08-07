from api.api_call import ApiCall
from config.config import URL


class GetBookingsAPI(ApiCall):
    path = URL.BOOKING_ROUTE

    def __init__(self, headers=None, query_params=None,  **kwargs):
        super().__init__(method='get', headers=headers, query_params=query_params, **kwargs)
