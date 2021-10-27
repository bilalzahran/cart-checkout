from fastapi import Depends
from dependency_injector.wiring import inject, Provide

from src.dependency.container import Container
from src.repository.product import ProductRepository
from src.repository.order import OrderRepository
from src.model.order import OrderRequestSchema, OrderOut


@inject
async def add_to_cart(
    payload: OrderRequestSchema,
    order_repo: OrderRepository = Depends(Provide[Container.order_repo]),
):
    # Check if order with status IN_CART exist
    # The status indicate order that has not been checked out by user / still in cart
    order: OrderOut = await order_repo.get_by_status_and_user_id(
        status="IN_CART", user_id=payload.user_id
    )

    if order:
        return order.id

    return {"Message": "Data no exist"}
