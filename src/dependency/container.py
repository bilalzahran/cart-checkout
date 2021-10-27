from databases import Database

from src.datasource.postgresql.db_manager import DbManager
from src.datasource.postgresql.model.users import Users
from src.datasource.postgresql.model.product import Product
from src.datasource.postgresql.model.orders import Order
from src.datasource.postgresql.model.detail_order import OrderDetail

from src.repository.product import ProductRepository
from src.repository.order import OrderRepository

from dependency_injector import containers, providers

from src.dependency.config import DB_URI
from src.utils.log_helper import LogHelper


class Container(containers.DeclarativeContainer):
    log_helper = providers.Singleton(LogHelper)

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

    product_repo: ProductRepository = providers.Singleton(
        ProductRepository, db_manager=db_manager
    )

    order_repo: OrderRepository = providers.Singleton(
        OrderRepository, db_manager=db_manager
    )
