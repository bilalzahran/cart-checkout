from sqlalchemy.sql.expression import false, null
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import Column, MetaData, Table
from sqlalchemy.sql.sqltypes import DateTime, Numeric, String


class Product:
    def __init__(self):
        metadata = MetaData()

        self.__table = Table(
            "products",
            metadata,
            Column("id", Numeric(), primary_key=True),
            Column("name", String(), nullable=False),
            Column("description", String(), nullable=True),
            Column("stock", Numeric(), default=0, nullable=False),
            Column("price", Numeric(), nullable=False),
            Column("version", Numeric(), nullable=False),
            Column("created_at", DateTime(timezone=False), default=func.now()),
            Column("updated_at", DateTime(timezone=False)),
        )

        self.id = self.__table.c.id
        self.name = self.__table.c.name
        self.description = self.__table.c.description
        self.stock = self.__table.c.stock
        self.price = self.__table.c.price
        self.version = self.__table.c.version
        self.created_at = self.__table.c.created_at
        self.updated_at = self.__table.c.updated_at

    def __call__(self):
        return self.__table
