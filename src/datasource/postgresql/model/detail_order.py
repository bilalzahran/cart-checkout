from sqlalchemy.sql.schema import Column, ForeignKey, MetaData, Table
from sqlalchemy.sql.sqltypes import Integer


class OrderDetail:
    def __init__(self):
        metadata = MetaData()

        self.__table = Table(
            "detail_order",
            metadata,
            Column("id", Integer(), primary_key=True, autoincrement=True),
            Column("order_id", Integer(), ForeignKey("orders.id"), nullable=False),
            Column("product_id", Integer(), nullable=False),
            Column("quantity", Integer(), nullable=False),
            Column("sub_total", Integer(), nullable=False),
        )

        self.id = self.__table.c.id
        self.order_id = self.__table.c.order_id
        self.product_id = self.__table.c.product_id
        self.quantity = self.__table.c.quantity
        self.sub_total = self.__table.c.sub_total

    def __call__(self):
        return self.__table
