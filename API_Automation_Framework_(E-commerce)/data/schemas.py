{
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
    "image": {
      "type": "string",
      "format": "uri"
    },
    "rating": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "rate": { "type": "number" },
            "count": { "type": "integer" }
          },
          "required": ["rate", "count"],
          "additionalProperties": false
        },
        {
          "type": "number"
        }
      ]
    }
  },
  "required": [
    "id",
    "title",
    "price",
    "description",
    "category",
    "image",
    "rating"
  ],
  "additionalProperties": false
}

