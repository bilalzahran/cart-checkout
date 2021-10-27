from src.datasource.postgresql.db_manager import DbManager
from src.utils.log_helper import LogHelper
from src.model.order import OrderOut, OrderWithDetail, OrderIn


class OrderRepository:
    def __init__(self, db_manager: DbManager):
        self.db = db_manager.db
        self.order = db_manager.order
        self.order_detail = db_manager.order_detail

    async def get_all(self):
        try:
            query = self.order().select()
            rows = await self.db.fetch_all(query=query)
            return (OrderOut(**row) for row in rows)
        except Exception as e:
            LogHelper.log_error(e)
            return False

    async def insert(self, payload: OrderIn):
        try:
            query = self.order().insert().values(**payload.dict(exclude=False))
            id = await self.db.execute(query=query)
            return id
        except Exception as e:
            LogHelper.log_error(e)
            return False
