from fastapi import APIRouter

from src.handler.api_handler.v1 import product, order

api_router = APIRouter()
api_router.include_router(
    product.product_routes,
    prefix=f"/{product.product_tag}",
    tags=[product.product_tag],
)

api_router.include_router(
    order.order_routes,
    prefix=f"/{order.order_tag}",
    tags=[order.order_tag],
)

v1_modules = [product, order]
