from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

product_one = Product(id=1, name="Product One", price=9.99, in_stock=True)
product_two = Product(id=2, name="Product Two", price=19.99)

# product_three = Product(name="Product Three") # errors: missing field 'id' and 'price'
