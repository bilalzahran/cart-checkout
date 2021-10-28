from typing import Any, List, Optional, Union
from pydantic import BaseModel
from datetime import datetime

from sqlalchemy.sql.expression import null


class DetailOrderRequestSchema(BaseModel):
    product_id: int
    quantity: int


class OrderRequestSchema(BaseModel):
    user_id: int
    order_detail: List[DetailOrderRequestSchema]


class OrderCheckoutRequestSchema(BaseModel):
    user_id: int


class Order(BaseModel):
    id: int
    order_sn: Optional[str]
    user_id: int
    total_amount: Optional[int]
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
    status: str = "IN_CART"
    total_amount: Optional[int]
    created_at: datetime = datetime.now()


class OrderDetail(DetailOrderRequestSchema):
    sub_total: int
    order_id: Union[int, None]
