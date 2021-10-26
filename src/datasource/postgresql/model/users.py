from sqlalchemy import MetaData, Table, Column
from sqlalchemy.sql.expression import false
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.sqltypes import DateTime, String, Numeric


class Users:
    def __init__(self):
        metadata = MetaData()

        self.__table = Table(
            "users",
            metadata,
            Column("id", Numeric(), primary_key=True),
            Column("name", String(), nullable=False),
            Column("phone", String(), nullable=False),
            Column("address", String(), nullable=False),
            Column(
                "created_at",
                DateTime(timezone=False),
                server_default=func.now(),
                nullable=False,
            ),
            Column("updated_at", DateTime(timezone=False)),
        )

        self.id = self.__table.c.id
        self.name = self.__table.c.name
        self.phone = self.__table.c.phone
        self.address = self.__table.c.phone
        self.created_at = self.__table.c.created_at
        self.updated_at = self.__table.c.update_at

    def __call__(self):
        return self.__table
