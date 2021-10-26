import os
from pydantic import BaseSettings
from sqlalchemy.engine.url import URL
from dotenv import load_dotenv


class __Config(BaseSettings):
    load_dotenv()
    db_users = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_driver = os.getenv("DB_DRIVER")

    class Config:
        case_sensitive = False


config = __Config()

DB_URI = URL(
    drivername=config.db_driver,
    username=config.db_users,
    password=config.db_password,
    host=config.db_host,
    port=config.db_port,
    database=config.db_name,
).__to_string__
