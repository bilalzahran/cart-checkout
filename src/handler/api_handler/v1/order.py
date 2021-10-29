from fastapi import APIRouter, status
from starlette.responses import Response
from src.model.order import (
    OrderRequestSchema,
    OrderCheckoutRequestSchema,
    OrderPaymentRequestSchema,
)
from src.service.order import (
    add_to_cart,
    checkout,
    update_payment_status,
    get_order_by_id as get_order_id,
)

order_routes = APIRouter()
order_tag = "order"


@order_routes.get("/")
async def get_order_by_id(order_id: int):
    response = await get_order_id(order_id)
    return response


@order_routes.post("/add-item")
async def add_item(payload: OrderRequestSchema):
    response = await add_to_cart(payload)
    return response


@order_routes.post("/checkout")
async def checkout_order(payload: OrderCheckoutRequestSchema, response: Response):
    response_data = await checkout(payload)
    return response_data


@order_routes.post("/update-payment")
async def update_payment_order(payload: OrderPaymentRequestSchema):
    response_data = await update_payment_status(payload)
    return response_data
