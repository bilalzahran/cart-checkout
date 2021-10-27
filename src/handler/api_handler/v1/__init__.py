from fastapi import APIRouter

from src.handler.api_handler.v1 import product

api_router = APIRouter()
api_router.include_router(
    product.product_routes,
    prefix=f"/v1/{product.product_tag}",
    tags=[product.product_tag],
)

v1_modules = [product]
