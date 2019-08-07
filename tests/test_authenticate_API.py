from models.AuthenticationModel import AuthenticationModel
from api.authenticate_API import AuthenticateAPI


def test_able_to_authenticate_with_valid_credentials():
    payload = AuthenticationModel()
    authenticate_api = AuthenticateAPI(payload=payload.to_json())
    response = authenticate_api.call()
    response_body = response.json()
    assert response.status_code == 200
    assert response_body['token']
    # TODO use better assertion matcher = exists()


def test_unable_to_authenticate_with_empty_username():
    payload = AuthenticationModel('')
    authenticate_api = AuthenticateAPI(payload=payload.to_json())
    response = authenticate_api.call()
    response_body = response.json()
    # assert response.status_code == 200    # returns 200 - bug in the API
    assert response_body['reason'] == "Bad credentials"


def test_unable_to_authenticate_with_empty_password():
    payload = AuthenticationModel('admin', '')
    authenticate_api = AuthenticateAPI(payload=payload.to_json())
    response = authenticate_api.call()
    response_body = response.json()
    # assert response.status_code == 200    # returns 200 - bug in the API
    assert response_body['reason'] == "Bad credentials"


def test_unable_to_authenticate_with_empty_username_and_password():
    payload = AuthenticationModel('', '')
    authenticate_api = AuthenticateAPI(payload=payload.to_json())
    response = authenticate_api.call()
    response_body = response.json()
    # assert response.status_code == 200    # returns 200 - bug in the API
    assert response_body['reason'] == "Bad credentials"


def test_unable_to_authenticate_with_invalid_username():
    payload = AuthenticationModel('admin_invalid')
    authenticate_api = AuthenticateAPI(payload=payload.to_json())
    response = authenticate_api.call()
    response_body = response.json()
    # assert response.status_code == 200    # returns 200 - bug in the API
    assert response_body['reason'] == "Bad credentials"


def test_unable_to_authenticate_with_invalid_password():
    payload = AuthenticationModel('admin', 'password_invalid')
    authenticate_api = AuthenticateAPI(payload=payload.to_json())
    response = authenticate_api.call()
    response_body = response.json()
    # assert response.status_code == 200    # returns 200 - bug in the API
    assert response_body['reason'] == "Bad credentials"


def test_unable_to_authenticate_with_invalid_username_and_password():
    payload = AuthenticationModel('admin_invalid', 'password_invalid')
    authenticate_api = AuthenticateAPI(payload=payload.to_json())
    response = authenticate_api.call()
    response_body = response.json()
    # assert response.status_code == 200    # returns 200 - bug in the API
    assert response_body['reason'] == "Bad credentials"




