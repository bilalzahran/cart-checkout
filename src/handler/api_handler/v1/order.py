from fastapi import APIRouter
from src.model.order import OrderRequestSchema
from src.service.order import add_to_cart

order_routes = APIRouter()
order_tag = "order"


@order_routes.post("/add-item")
async def add_item(payload: OrderRequestSchema):
    response = await add_to_cart(payload)
    return response
