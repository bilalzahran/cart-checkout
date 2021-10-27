from src.datasource.postgresql.db_manager import DbManager
from src.model.order import DetailOrder
from src.utils.log_helper import LogHelper


class OrderDetailRepository:
    def __init__(self, db_manager: DbManager):
        self.db = db_manager.db
        self.order_detail = db_manager.order_detail

    async def insert(self, payload: DetailOrder):
        try:
            query = self.order_detail().insert().values(**payload.dict(exclude=False))
            id = self.db.execute(query=query)
            return id
        except Exception as ex:
            LogHelper.log_error(ex)
            return False
