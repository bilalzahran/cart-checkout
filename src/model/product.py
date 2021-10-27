from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ProductRequestSchema(BaseModel):
    name: str
    description: Optional[str]
    stock: Optional[int]
    price: Optional[int]
    version: Optional[int]


class ProductIn(ProductRequestSchema):
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime]


class ProductOut(ProductIn):
    id: int
