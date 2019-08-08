from models.AuthenticationModel import AuthenticationModel
from api.authenticate_API import AuthenticateAPI
from api.delete_booking_API import DeleteBookingAPI


def test_delete_booking_API():
    auth_payload = AuthenticationModel()
    authenticate_api = AuthenticateAPI(payload=auth_payload.to_json())
    auth_response = authenticate_api.call()
    auth_response_body = auth_response.json()
    token = auth_response_body['token']

    delete_booking_API = DeleteBookingAPI(6)
    delete_booking_API.headers['cookie'] = f"token={token}"
    delete_response = delete_booking_API.call()
    assert delete_response.status_code == 201


def test_delete_non_existing_booking():
    auth_payload = AuthenticationModel()
    authenticate_api = AuthenticateAPI(payload=auth_payload.to_json())
    auth_response = authenticate_api.call()
    auth_response_body = auth_response.json()
    token = auth_response_body['token']

    delete_booking_API = DeleteBookingAPI(69)
    delete_booking_API.headers['cookie'] = f"token={token}"
    delete_response = delete_booking_API.call()
    assert delete_response.status_code == 405

