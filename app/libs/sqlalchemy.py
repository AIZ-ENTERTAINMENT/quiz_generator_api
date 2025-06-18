from app.libs.serializer import json_dumps

engine_option = {
    "echo": False,
    "json_serializer": lambda data: json_dumps(data, indent=None),
    "pool_size": 3,
    "max_overflow": 6,
    "pool_recycle": 600,
    "connect_args": {
        "charset": "utf8mb4",
    },
}
