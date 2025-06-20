from os import environ

from app.libs.database import configure_sqlalchemy
from app.libs.logger_config import set_logger, studio_be_logger_name

_db_uri = f"mysql+aiomysql://{environ['DB_USER']}:{environ['DB_PWD']}@{environ['DB_HOST']}:3306/quiz_generator"

configure_sqlalchemy(
    connection_uri=_db_uri,
    engine_options={
        "pool_size": 10,
        "max_overflow": 20,
        "pool_timeout": 30,
        "pool_recycle": 3600,
    },
)

set_logger(logger_name=studio_be_logger_name)
