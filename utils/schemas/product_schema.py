"""
JSON Schema для валидации ответа от эндпоинта GET /api/Products
"""

GET_PRODUCTS_SCHEMA = {
    "type": "object",
    "properties": {
        "status": {"type": "string"},
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "description": {"type": "string"},
                    "price": {"type": "number"}
                },
                "required": ["id", "name", "price"] # Эти поля обязаны быть у каждого товара!
            }
        }
    },
    "required": ["status", "data"]
}