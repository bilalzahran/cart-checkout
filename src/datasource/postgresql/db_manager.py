from databases import Database

from src.datasource.postgresql.model.users import Users
from src.datasource.postgresql.model.product import Product
from src.datasource.postgresql.model.orders import Order
from src.datasource.postgresql.model.detail_order import OrderDetail


class DbManager:
    def __init__(
        self,
        users: Users,
        product: Product,
        order: Order,
        order_detail: OrderDetail,
        database: Database,
    ):
        self.users = users
        self.product = product
        self.order = order
        self.order_detail = order_detail
        self.db = database
