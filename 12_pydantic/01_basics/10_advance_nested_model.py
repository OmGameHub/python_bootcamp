from pydantic import BaseModel
from typing import Optional, List, Union

class Address(BaseModel):
    street: str
    city: str
    pincode: str


class Company(BaseModel):
    name: str
    address: Optional[Address] = None


class Employee(BaseModel):
    name: str
    company: Optional[Company] = None

class TextContent(BaseModel):
    type: str = "text"
    content: str

class ImageContent(BaseModel):
    type: str = "image_url"
    url: str
    alt_text: str

class Article(BaseModel):
    title: str
    content: Union[TextContent, ImageContent]

class Country(BaseModel):
    name: str
    code: str

class State(BaseModel):
    name: str
    code: str
    country: Country

class City(BaseModel):
    name: str
    code: str
    state: State

class Address(BaseModel):
    street: str
    city: City
    pincode: str

class Organization(BaseModel):
    name: str
    headquarters: Address
    branches: List[Address] = []