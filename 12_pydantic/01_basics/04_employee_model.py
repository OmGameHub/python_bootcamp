from pydantic import BaseModel, Field
from typing import Optional
import re

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Employee name",
        example="Om Prakash"
    )
    department: Optional[str] = "General"
    salary: float = Field(
        ...,
        ge=10000,
        description="Employee salary in USD",
        example=50000.0
    )

class User(BaseModel):
    id: int
    name: str
    email: str = Field(
        ...,
        regex=r'^[\w\.-]+@[\w\.-]+\.\w+$',
        description="User email address",
        example="omprakash@example.com"
    )
    phone: str = Field(
        ...,
        regex=r'^\+?1?\d{9,15}$',
        description="User phone number",
        example="+1234567890"
    )
    age: int = Field(
        ...,
        ge=0,
        le=120,
        description="Age in years",
        example=30
    )
    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="User discount",
        example=10.0
    )