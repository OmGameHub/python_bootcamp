from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime

class Person(BaseModel):
    first_name: str
    last_name: str

    @field_validator("first_name", "last_name")
    def names_must_be_capitalized(cls, value):
        if not value.istitle():
            raise ValueError("Names must be capitalized")
        return value
    
class User(BaseModel):
    email: str

    @field_validator("email")
    def normalize_email(cls, value):
        return value.strip().lower()
    

class Product(BaseModel):
    price: str # $4.44

    @field_validator("price", mode="before")
    def parse_price(cls, value):
        if isinstance(value, str):
            value = value.strip().replace("$", "")
        return float(value)
    

class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    @model_validator(mode="after")
    def validate_dates(cls, values):
        if values["start_date"] >= values["end_date"]:
            raise ValueError("End date must be after start date")
        return values
