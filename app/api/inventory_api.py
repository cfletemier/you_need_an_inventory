from flask_restful import request, Resource
from jsonschema import validate, ValidationError

from flask import (
    current_app as app,
    jsonify,
    make_response,
)


from app.models.models import (
    Item,
    ItemType,
)
from app import db
from app.api.schemas import INVENTORY_CREATE_SCHEMA


def validate_payload(request, schema):
    """
    Given a request and a schema, perform schema validation
    :param request: request object
    :param schema: jsonschema
    :return: json version of request payload
    """
    try:
        schema.validate(request.json)
    except ValidationError:
        raise

    return request.json


def generate_response(message, status):
    return make_response(jsonify(message), status)


def render_item(item):
    return {
        'id': item.id,
        'title': item.title,
        'itemType': item.item_type.item_type,
        'dateAdded': item.date_added,
        'dateRemoved': item.date_removed,
        'inPossession': item.in_possession,
    }


class HelloWorld(Resource):
    def get(self):
        return "hello world!"


class ItemTypeHandler(Resource):
    def get(self):
        item_types = ItemType.query.all()
        return generate_response([item.item_type for item in item_types], 200)


class InventoryHandler(Resource):
    def post(self):
        try:
            payload = validate_payload(request, INVENTORY_CREATE_SCHEMA)
        except ValidationError as ex:
            return generate_response(ex.message, 400)

        item_type = ItemType.query.filter_by(item_type=payload['itemType']).first()

        if not item_type:
            return generate_response(
                "{item_type} is not one of the valid types".format(item_type=payload['itemType']),
                404
            )

        item = Item(
            item_type=item_type,
            title=payload['title']
        )
        db.session.add(item)
        db.session.commit()

        return make_response("Created", 201)

    def get(self, inventory_id):
        item = Item.query.filter_by(id=inventory_id).first()
        if not item:
            return generate_response('Not found', 404)

        return generate_response(render_item(item), 200)
