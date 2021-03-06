from sqlalchemy.sql.functions import user
from src.datasource.postgresql.db_manager import DbManager
from src.utils.log_helper import LogHelper
from src.model.order import Order, OrderIn


class OrderRepository:
    def __init__(self, db_manager: DbManager):
        self.db = db_manager.db
        self.order = db_manager.order
        self.order_detail = db_manager.order_detail

    async def get_all(self):
        try:
            query = self.order().select()
            rows = await self.db.fetch_all(query=query)
            return (Order(**row) for row in rows)
        except Exception as e:
            LogHelper.log_error(e)
            return False

    async def get_by_status_and_user_id(self, status, user_id) -> Order:
        try:
            query = (
                self.order()
                .select()
                .where(self.order.status == status)
                .where(self.order.user_id == user_id)
            )
            row = await self.db.fetch_one(query=query)
            return Order(**row)
        except Exception as ex:
            LogHelper.log_error(ex)
            return False

    async def get_order_by_id(self, order_id) -> Order:
        try:
            query = self.order().select().where(self.order.id == order_id)
            row = await self.db.fetch_one(query=query)
            return Order(**row)
        except Exception as ex:
            LogHelper.log_error(ex)
            return False

    async def insert(self, payload: OrderIn):
        try:
            query = self.order().insert().values(**payload.dict(exclude=False))
            id = await self.db.execute(query=query)
            return id
        except Exception as e:
            LogHelper.log_error(e)
            return False

    async def update(self, payload: Order):
        print(payload)
        try:
            query = (
                self.order()
                .update()
                .where(self.order.id == payload.id)
                .values(payload.dict(exclude=False))
            )
            await self.db.execute(query=query)
            return True
        except Exception as ex:
            LogHelper.log_error(ex)
            return False
