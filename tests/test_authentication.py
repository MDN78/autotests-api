from http import HTTPStatus
from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginResponseSchema, LoginRequestSchema
from tests.conftest import UserFixture
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
import pytest


@pytest.mark.regression
@pytest.mark.authentication
def test_login(function_user: UserFixture, authentication_client: AuthenticationClient):
    # Аутентифицируемся созданным пользователем
    request = LoginRequestSchema(email=function_user.email, password=function_user.password)
    response = authentication_client.login_api(request)
    response_data = LoginResponseSchema.model_validate_json(response.text)

    # Проверяем статус-код ответа
    assert_status_code(response.status_code, HTTPStatus.OK)
    # Проверяем корректность тела ответа
    assert_login_response(response_data)
    # валидация JSON-схемы
    validate_json_schema(response.json(), response_data.model_json_schema())
