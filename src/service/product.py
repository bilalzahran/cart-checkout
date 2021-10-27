from fastapi.params import Depends
from dependency_injector.wiring import inject, Provide

from src.dependency.container import Container
from src.repository.product import ProductRepository


@inject
async def get_all_products(
    product_repo: ProductRepository = Depends(Provide[Container.product_repo]),
):
    return await product_repo.get_all()
