from pydantic import BaseModel
from typing import List, Optional


class Address(BaseModel):
    street: str
    city: str
    pincode: str

class Person(BaseModel):
    id: int
    name: str
    address: Address

address = Address(street="123 Main St", city="Springfield", pincode="12345")
user = Person(id=1, name="John Doe", address=address)
print(user)

user_data = {
    "id": 1,
    "name": "Om Prakash",
    "address": {
        "street": "123 Main St",
        "city": "Springfield",
        "pincode": "12345"
    }
}
my_user = Person(**user_data)
print(my_user)