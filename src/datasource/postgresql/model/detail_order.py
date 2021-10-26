from sqlalchemy import MetaData
from sqlalchemy.sql.schema import Column, ForeignKey, Table
from sqlalchemy.sql.sqltypes import Numeric


class OrderDetail:
    def __init__(self):
        metadata = MetaData()

        self.__table = Table(
            "detail_order",
            metadata,
            Column("id", Numeric(), primary_key=True),
            Column("order_id", Numeric(), ForeignKey("orders.id"), nullable=False),
            Column("product_id", Numeric(), nullable=False),
            Column("quantity", Numeric(), nullable=False),
            Column("sub_total", Numeric(), nullable=False),
        )

        self.id = self.__table.c.id
        self.order_id = self.__table.c.order_id
        self.product_id = self.__table.c.product_id
        self.quantity = self.__table.c.quantity
        self.sub_total = self.__table.c.sub_total

    def __call__(self):
        return self.__table
