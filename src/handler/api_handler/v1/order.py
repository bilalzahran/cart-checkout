from fastapi import APIRouter, status
from starlette.responses import Response
from src.model.order import OrderRequestSchema, OrderCheckoutRequestSchema
from src.service.order import add_to_cart, checkout

order_routes = APIRouter()
order_tag = "order"


@order_routes.post("/add-item")
async def add_item(payload: OrderRequestSchema):
    response = await add_to_cart(payload)
    return response


@order_routes.post("/checkout")
async def checkout_order(payload: OrderCheckoutRequestSchema, response: Response):
    response_data = await checkout(payload)
    return response_data
