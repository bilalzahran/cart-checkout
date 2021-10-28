from typing import List
from src.datasource.postgresql.db_manager import DbManager
from src.model.order import OrderDetail
from src.utils.log_helper import LogHelper


class OrderDetailRepository:
    def __init__(self, db_manager: DbManager):
        self.db = db_manager.db
        self.order_detail = db_manager.order_detail

    async def insert(self, payload: OrderDetail):
        try:
            query = self.order_detail().insert().values(**payload.dict(exclude=False))
            id = await self.db.execute(query=query)
            return id
        except Exception as ex:
            LogHelper.log_error(ex)
            return False

    async def update(self, payload: OrderDetail, order_id: str):
        try:
            query = (
                self.order_detail()
                .update()
                .where(self.order_detail.product_id == payload.product_id)
                .where(self.order_detail.order_id == order_id)
                .values(**payload.dict(exclude=False))
            )
            await self.db.execute(query=query)
            return True
        except Exception as ex:
            LogHelper.log_error(ex)
            return False

    async def get_by_order_id_and_product_id(
        self, order_id: int, product_id: int
    ) -> OrderDetail:
        try:
            query = (
                self.order_detail()
                .select()
                .where(self.order_detail.order_id == order_id)
                .where(self.order_detail.product_id == product_id)
            )
            row = await self.db.fetch_one(query=query)
            return OrderDetail(**row)
        except Exception as ex:
            LogHelper.log_error(ex)
            return False

    async def get_by_order_id(self, order_id: int) -> List[OrderDetail]:
        try:
            query = (
                self.order_detail()
                .select()
                .where(self.order_detail.order_id == order_id)
            )
            rows = await self.db.fetch_all(query=query)
            return (OrderDetail(**row) for row in rows)
        except Exception as ex:
            LogHelper.log_error(ex)
            return False

   