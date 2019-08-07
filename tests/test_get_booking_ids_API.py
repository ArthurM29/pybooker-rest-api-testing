from api.get_bookings_ids_API import GetBookingIdsAPI


def test_get_all_bookings():
    get_booking_ids_api = GetBookingIdsAPI()
    response = get_booking_ids_api.call()
    assert response.status_code == 200


def test_get_bookings_by_name():
    query_params = {'firstname': 'Sally', 'lastname': "Ericsson"}
    get_bookings_id_api = GetBookingIdsAPI(query_params=query_params)
    response = get_bookings_id_api.call()
    bookings = response.json()

    assert response.status_code == 200
    assert len(bookings) == 1
    assert bookings[0]['bookingid'] == 1


def test_get_bookings_by_date():
    query_params = {'checkin': '2018-01-01', 'checkout': "2019-01-01"}
    get_booking_ids_api = GetBookingIdsAPI(query_params=query_params)
    response = get_booking_ids_api.call()
    bookings = response.json()

    assert response.status_code == 200
    assert len(bookings) == 1
    assert bookings[0]['bookingid'] == 3


def test_get_bookings_by_checkin_date_only():
    query_params = {'checkin': '2018-01-01'}
    get_booking_ids_api = GetBookingIdsAPI(query_params=query_params)
    response = get_booking_ids_api.call()
    bookings = response.json()

    assert response.status_code == 200
    assert len(bookings) == 5


def test_get_bookings_by_checkout_date_only():
    query_params = {'checkout': "2019-01-01"}
    get_booking_ids_api = GetBookingIdsAPI(query_params=query_params)
    response = get_booking_ids_api.call()
    bookings = response.json()

    assert response.status_code == 200
    assert len(bookings) == 4
