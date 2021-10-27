from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import Column, ForeignKey, MetaData, Table
from sqlalchemy.sql.sqltypes import DateTime, Numeric, String


class Order:
    def __init__(self):

        metadata = MetaData()

        self.__table = Table(
            "orders",
            metadata,
            Column("id", Numeric(), primary_key=True),
            Column("order_sn", String(), nullable=False),
            Column("user_id", Numeric(), ForeignKey("users.id"), nullable=False),
            Column("total_amount", Numeric(), nullable=False),
            Column("status", String(), nullable=False),
            Column("payment_status", String(), nullable=False),
            Column("payment_method", String(), nullable=False),
            Column("cancel_by", String(), nullable=True),
            Column("cancel_reason", String(), nullable=True),
            Column("payment_at", DateTime(timezone=False), nullable=True),
            Column(
                "created_at",
                DateTime(timezone=False),
                default=func.now(),
                nullable=False,
            ),
            Column("cancelled_at", DateTime(timezone=False), nullable=True),
            Column("updated_at", DateTime(timezone=False), nullable=True),
        )

        self.id = self.__table.c.id
        self.order_sn = self.__table.c.order_sn
        self.user_id = self.__table.c.user_id
        self.total_amount = self.__table.c.total_amount
        self.status = self.__table.c.status
        self.payment_status = self.__table.c.payment_status
        self.payment_method = self.__table.c.payment_method
        self.cancel_by = self.__table.c.cancel_by
        self.cancel_reason = self.__table.c.cancel_reason
        self.payment_at = self.__table.c.payment_at
        self.created_at = self.__table.c.created_at
        self.cancelled_at = self.__table.c.cancelled_at
        self.updated_at = self.__table.c.updated_at

    def __call__(self):
        return self.__table
