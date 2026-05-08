product_schema = {
    "type": "object",

    "properties": {
        "id": {
            "type": "integer",
            "minimum": 1
        },

        "title": {
            "type": "string",
            "minLength": 1
        },

        "price": {
            "type": "number",
            "exclusiveMinimum": 0
        },

        "description": {
            "type": "string",
            "minLength": 1
        },

        "category": {
            "type": "string",
            "minLength": 1
        },

        "rating": {
            "oneOf": [
                {
                    "type": "object",
                    "properties": {
                        "rate": {"type": "number"},
                        "count": {"type": "integer"}
                    },
                    "required": ["rate", "count"]
                },
                {
                    "type": "number"
                }
            ]
        },

        "image": {
            "type": "string"
        },

        "images": {
            "type": "array"
        },

        "thumbnail": {
            "type": "string"
        }
    },

    "required": [
        "id",
        "title",
        "price",
        "description",
        "category",
        "rating"
    ]
}
