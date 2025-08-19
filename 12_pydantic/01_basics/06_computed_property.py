from pydantic import BaseModel, Field, computed_field

class Product(BaseModel):
    name: str
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    
class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., gt=1)
    rate_per_night: float = Field(..., gt=0)

    @computed_field
    @property
    def total_price(self) -> float:
        return self.nights * self.rate_per_night

booking = Booking(
    user_id=1, 
    room_id=101, 
    nights=3, 
    rate_per_night=100.0
)
print(f"Total price for booking: ${booking.total_price:.2f}")
print(booking.model_dump())