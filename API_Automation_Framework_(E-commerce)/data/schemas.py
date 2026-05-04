product_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer", "minimum": 1},
        "title": {"type": "string", "minLength": 1},
        "price": {"type": "number", "exclusiveMinimum": 0},
        "description": {"type": "string", "minLength": 1},
        "category": {"type": "string", "minLength": 1},
        "image": {"type": "string", "format": "uri"},
        "rating": {
            "type": "object",
            "properties": {
                "rate": {"type": "number", "minimum": 0},
                "count": {"type": "integer", "minimum": 0}
            },
            "required": ["rate", "count"],
            "additionalProperties": False
        }
    },
    "required": ["id", "title", "price", "description", "category", "image", "rating"],
    "additionalProperties": False
}
