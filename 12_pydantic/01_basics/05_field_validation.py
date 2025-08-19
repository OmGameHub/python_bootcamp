from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    username: str

    @field_validator("username")
    def validate_username(cls, value):
        if len(value) < 3:
            raise ValueError("Username must be at least 3 characters long")
        return value


class SignupData(BaseModel):
    email: str
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def password_match(cls, values):
        if values.get("password") != values.get("confirm_password"):
            raise ValueError("Passwords do not match")
        return values