from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:%S")
        }
    )

user = User(
    id=1,
    name="Om Prakash",
    email="om@example.com",
    created_at=datetime(2025, 8, 20, 1, 30),
    address=Address(
        street="123 Main St",
        city="New Delhi",
        zip_code="12345"
    ),
    is_active=True,
    tags=["developer", "javascript"]
)
print(f"User model: {user}")

print("-" * 200)


python_dict = user.model_dump()
print(f"Python dict: {python_dict}")

print("-" * 200)

json_data = user.model_dump_json()
print(f"JSON data: {json_data}")