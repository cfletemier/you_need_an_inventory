from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/you_need_an_inventory'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from app.models.models import db
    db.init_app(app)
    migrate = Migrate(app, db)

    from app.api.inventory_api import HelloWorld, ItemTypeHandler, InventoryCollectionHandler, InventoryHandler
    api = Api(app)
    api.add_resource(HelloWorld, '/')
    api.add_resource(ItemTypeHandler, '/item-types')
    api.add_resource(InventoryHandler, '/inventory/<int:inventory_id>')
    api.add_resource(InventoryCollectionHandler, '/inventory')

    return app
