from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]

class BlogPost(BaseModel):
    id: int
    title: str
    content: str
    image_url: Optional[str] = None

card_data = {
    "user_id": 1,
    "items": ["Laptop", "Mouse"],
    "quantities": {"Laptop": 2, "Mouse": 1}
}

cart = Cart(**card_data)
