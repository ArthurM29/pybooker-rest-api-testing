from models.BookingModel import BookingModel
from api.create_booking_API import CreateBookingAPI


def test_create_booking_with_defaults():
    payload = BookingModel()
    create_booking_api = CreateBookingAPI(payload=payload.to_json())
    response = create_booking_api.call()
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['booking']['firstname'] == 'Jim'
    assert response_body['booking']['lastname'] == 'Brown'
    assert response_body['booking']['totalprice'] == 111
    assert response_body['booking']['depositpaid'] == True
    assert response_body['booking']['bookingdates']['checkin'] == '2018-01-01'
    assert response_body['booking']['bookingdates']['checkout'] == '2018-01-14'
    assert response_body['booking']['additionalneeds'] == 'Breakfast'


def test_create_booking_with_custom_name():
    payload = BookingModel(first_name='Salma', last_name='Hayek')
    create_booking_api = CreateBookingAPI(payload=payload.to_json())
    response = create_booking_api.call()
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['booking']['firstname'] == 'Salma'
    assert response_body['booking']['lastname'] == 'Hayek'


def test_create_booking_with_booking_dates():
    payload = BookingModel()
    payload.bookingdates.checkin = '2019-09-19'
    payload.bookingdates.checkout = '2019-09-29'
    create_booking_api = CreateBookingAPI(payload=payload.to_json())
    response = create_booking_api.call()
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['booking']['bookingdates']['checkin'] == '2019-09-19'
    assert response_body['booking']['bookingdates']['checkout'] == '2019-09-29'
