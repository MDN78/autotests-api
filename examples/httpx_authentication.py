import httpx

# Инициализируем JSON-данные, которые будем отправлять в API
login_payload = {
    "email": "test-user@example.com",
    "password": "123456"
}

# Выполняем POST-запрос к эндпоинту /api/v1/authentication/login
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

# Выводим JSON-ответ и статус-код
print("login response: ", login_response_data)
print("Status Code: ", login_response.status_code)


# Формируем payload для обновления токена
refresh_payload = {
    "refreshToken": login_response_data["token"]["refreshToken"]
}

# Выполняем запрос на обновление токена
refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()

# Выводим обновленные токены
print("Refresh response:", refresh_response_data)
print("Status Code:", refresh_response.status_code)