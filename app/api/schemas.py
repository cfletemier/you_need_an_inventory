from jsonschema import Draft4Validator

INVENTORY_CREATE_SCHEMA = Draft4Validator(
    schema={
        "type": "object",
        "properties": {
            "title": {
                "type": "string",
                "minLength": 1,
            },
            "itemType": {
                "type": "string"
            }
        },
        "required": ["title", "itemType"]
    }
)
