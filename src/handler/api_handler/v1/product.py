from src.model.product import ProductIn

from fastapi import APIRouter

from src.service.product import get_all_products

product_routes = APIRouter()
product_tag = "product"


@product_routes.get("/")
async def get_all():
    result = await get_all_products()
    return result
