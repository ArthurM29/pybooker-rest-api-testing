from models.AuthenticationModel import AuthenticationModel
from models.BookingModel import BookingModel
from api.authenticate_API import AuthenticateAPI
from api.update_booking_API import UpdateBookingAPI


def test_update_firstname_and_lastname():
    auth_payload = AuthenticationModel()
    authenticate_api = AuthenticateAPI(payload=auth_payload.to_json())
    auth_response = authenticate_api.call()
    auth_response_body = auth_response.json()
    token = auth_response_body['token']

    new_payload = BookingModel(first_name='Jack', last_name='Daniels')
    update_booking_API = UpdateBookingAPI(10, payload=new_payload.to_json())
    update_booking_API.headers['cookie'] = f"token={token}"
    update_response = update_booking_API.call()
    update_response_body = update_response.json()

    assert update_response.status_code == 200
    assert update_response_body['firstname'] == 'Jack'
    assert update_response_body['lastname'] == 'Daniels'











