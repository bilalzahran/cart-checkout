from src.datasource.postgresql.db_manager import DbManager
from src.model.product import ProductOut, ProductIn
from typing import List
from src.utils.log_helper import LogHelper


class ProductRepository:
    def __init__(self, db_manager: DbManager):
        self.db = db_manager.db
        self.product = db_manager.product

    async def get_all(self) -> List[ProductOut]:
        try:
            query = self.product().select()
            rows = await self.db.fetch_all(query=query)
            return (ProductOut(**row) for row in rows)
        except Exception as ex:
            LogHelper.log_error(ex)

    async def get_one(self, product_id) -> ProductOut:
        try:
            query = self.product().select().where(self.product.id == product_id)
            row = await self.db.fetch_one(query=query)
            if not row:
                return None
            return ProductOut(**row)

        except Exception as ex:
            LogHelper.log_error(ex)
            return False

    async def get_product_by_id(self, product_id_list) -> List[ProductOut]:
        try:
            query = self.product().select().where(self.product.id.in_(product_id_list))
            rows = await self.db.fetch_all(query=query)
            return (ProductOut(**row) for row in rows)

        except Exception as ex:
            LogHelper.log_error(ex)
            return False

    async def insert(self, payload: ProductIn):
        try:
            query = self.product().insert().values(**payload.dict(exclude=False))
            id = await self.db.execute(query=query)
            return id
        except Exception as ex:
            LogHelper.log_error(ex)
            return False

    async def update(self, payload: ProductIn, product_id: int):
        try:
            query = (
                self.product()
                .update()
                .where(self.product.id == product_id)
                .values(payload)
            )
            await self.db.execute(query=query)
            return True
        except Exception as ex:
            LogHelper.log_error(ex)
            return False

    async def bulk_update(self, payload: List[ProductOut]):
        try:
            for item in payload:
                query = (
                    self.product()
                    .update()
                    .where(self.product.id == item.id)
                    .where(self.product.version == item.version - 1)
                    .values(item.dict(exclude=False))
                )
                await self.db.execute(query=query)
            return True
        except Exception as ex:
            LogHelper.log_error(ex)
            return False
