import jsonschema

from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertion.schema import validate_json_schema
from tools.fakers import fake

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
create_user_response = public_users_client.create_user_api(create_user_request)
# Получаем JSON-схему из Pydantic-модели ответа
create_user_response_schema = CreateUserResponseSchema.model_json_schema()
# print(create_user_response_schema)
# print(create_user_response.json())

# Проверяем, что JSON-ответ от API соответствует ожидаемой JSON-схеме
jsonschema.validate(instance=create_user_response.json(), schema=create_user_response_schema)

# Используем нашу функцию из Tools место примера выше
validate_json_schema(instance=create_user_response.json(), schema=create_user_response_schema)