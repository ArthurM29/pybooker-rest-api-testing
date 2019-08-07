from api.get_bookings_API import GetBookingsAPI


def test_get_all_bookings():
    get_bookings_api = GetBookingsAPI()
    response = get_bookings_api.call()
    assert response.status_code == 200


def test_get_bookings_by_name():
    query_params = {'firstname': 'Sally', 'lastname': "Ericsson"}
    get_bookings_api = GetBookingsAPI(query_params=query_params)
    response = get_bookings_api.call()
    bookings = response.json()

    assert response.status_code == 200
    assert len(bookings) == 1
    assert bookings[0]['bookingid'] == 1


def test_get_bookings_by_date():
    query_params = {'checkin': '2018-01-01', 'checkout': "2019-01-01"}
    get_bookings_api = GetBookingsAPI(query_params=query_params)
    response = get_bookings_api.call()
    bookings = response.json()

    assert response.status_code == 200
    assert len(bookings) == 1
    assert bookings[0]['bookingid'] == 3


def test_get_bookings_by_checkin_date_only():
    query_params = {'checkin': '2018-01-01'}
    get_bookings_api = GetBookingsAPI(query_params=query_params)
    response = get_bookings_api.call()
    bookings = response.json()

    assert response.status_code == 200
    assert len(bookings) == 5


def test_get_bookings_by_checkout_date_only():
    query_params = {'checkout': "2019-01-01"}
    get_bookings_api = GetBookingsAPI(query_params=query_params)
    response = get_bookings_api.call()
    bookings = response.json()

    assert response.status_code == 200
    assert len(bookings) == 4