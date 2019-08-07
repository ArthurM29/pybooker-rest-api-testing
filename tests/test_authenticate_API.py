from models.AuthenticationModel import AuthenticationModel
from api.authenticate_API import AuthenticateAPI


def test_authenticate_with_valid_credentials():
    payload = AuthenticationModel()
    authenticate_api = AuthenticateAPI(payload=payload.to_json())
    response = authenticate_api.call()
    # response_body = response.json()
    assert response.status_code == 200
    # assert response_body['token'] == 'Mary'



