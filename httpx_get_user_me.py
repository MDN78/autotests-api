import httpx

# Get access token
login_payload = {
    "email": "test-user@example.com",
    "password": "123456"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login",
                            json=login_payload)

login_response_data = login_response.json()
access_token = login_response_data["token"]["accessToken"]

print("Status Code: ", login_response.status_code)
print("login response: ", login_response_data)

# Get info
headers = {
    "Authorization": f"Bearer {access_token}"
}

get_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

get_me_response_data = get_me_response.json()

print("Status Code: ", get_me_response.status_code)
print("Users info me view: ", get_me_response_data)
