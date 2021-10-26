from databases import Database

from src.datasource.postgresql.db_manager import DbManager
from src.datasource.postgresql.model.users import Users
from src.datasource.postgresql.model.product import Product
from src.datasource.postgresql.model.orders import Order
from src.datasource.postgresql.model.detail_order import OrderDetail

from dependency_injector import containers, providers

from src.dependency.config import DB_URI


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    database = providers.Singleton(Database, DB_URI)

    users = providers.Singleton(Users)
    product = providers.Singleton(Product)
    order = providers.Singleton(Order)
    order_detail = providers.Singleton(OrderDetail)

    db_manager = providers.Singleton(
        DbManager,
        database=database,
        users=users,
        product=product,
        order=order,
        order_detail=order_detail,
    )
