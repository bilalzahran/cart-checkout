from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ProductIn(BaseModel):
    name: str
    description: Optional[str]
    stock: Optional[int]
    price: Optional[int]
    version: Optional[int]
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime]


class ProductOut(ProductIn):
    id: int
