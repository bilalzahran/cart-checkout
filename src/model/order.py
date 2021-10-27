from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class OrderOut(BaseModel):
    id: int
    order_sn: str
    user_id: int
    total_amount: int
    status: Optional[str]
    payment_status: Optional[str]
    payment_method: Optional[str]
    cancel_by: Optional[str]
    cancel_reason: Optional[str]
    payment_at: Optional[datetime]
    cancelled_at: Optional[datetime]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class OrderIn(BaseModel):
    user_id: int
    status: str
    created_at: datetime


class DetailOrderRequestSchema(BaseModel):
    product_id: int
    quantity: int


class OrderRequestSchema(BaseModel):
    user_id: int
    order_detail: List[DetailOrderRequestSchema]
    status: str = "IN_CART"
    created_at: datetime = datetime.now()
