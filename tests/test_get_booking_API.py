from api.get_booking_API import GetBookingAPI
import pytest


def test_get_booking_10():
    get_booking_api = GetBookingAPI(10)
    response = get_booking_api.call()
    booking = response.json()
    assert response.status_code == 200
    assert booking['firstname'] == 'Mary'
    assert booking['lastname'] == 'Smith'


@pytest.mark.skip
def test_get_booking_with_invalid_id():
    get_booking_api = GetBookingAPI(1999)
    response = get_booking_api.call()
    print(f"RESPONSE: {response}, type: {type(response)}")
    assert response.status_code == 404

