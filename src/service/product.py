from fastapi.params import Depends
from dependency_injector.wiring import inject, Provide

from src.dependency.container import Container
from src.repository.product import ProductRepository

from src.model.product import ProductRequestSchema, ProductIn


@inject
async def get_all_products(
    product_repo: ProductRepository = Depends(Provide[Container.product_repo]),
):
    return await product_repo.get_all()


@inject
async def insert_product(
    payload: ProductRequestSchema,
    product_repo: ProductRepository = Depends(Provide[Container.product_repo]),
):
    db_payload = ProductIn(**payload.dict(exclude=False))
    return await product_repo.insert(db_payload)
