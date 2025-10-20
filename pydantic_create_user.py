from pydantic import BaseModel, Field, EmailStr
import uuid


class UserSchema(BaseModel):
    """
    Модель данных пользователя
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Unique user identifier")
    email: EmailStr
    last_name: str = Field(alias="lastName", min_length=1, max_length=50, description="User's last name")
    first_name: str = Field(alias="firstName", min_length=1, max_length=50, description="User's first name")
    middle_name: str = Field(alias="middleName", min_length=1, max_length=50, description="User's middle name")


class CreateUserRequestSchema(BaseModel):
    """
    Модель запроса на создание пользователя
    """
    email: EmailStr
    password: str = Field(min_length=1, max_length=250, description="User password (min 1, max 250 characters)")
    last_name: str = Field(alias="lastName", min_length=1, max_length=50, description="User's last name")
    first_name: str = Field(alias="firstName", min_length=1, max_length=50, description="User's first name")
    middle_name: str = Field(alias="middleName", min_length=1, max_length=50, description="User's middle name")


class CreateUserResponseSchema(BaseModel):
    """
    Модель ответа с данными созданного пользователя
    """
    user: UserSchema = Field(description="User data")
