from src.model.product import ProductIn

from fastapi import APIRouter

from src.service.product import get_all_products, insert_product
from src.model.product import ProductRequestSchema

product_routes = APIRouter()
product_tag = "product"


@product_routes.get("/")
async def get_all_product():
    result = await get_all_products()
    return result


@product_routes.post("/")
async def add_product(payload: ProductRequestSchema):
    result = await insert_product(payload)
    return result
