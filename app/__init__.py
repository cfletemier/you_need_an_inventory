from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()


def init_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/you_need_an_inventory'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from app.models.models import db
    db.init_app(app)
    migrate = Migrate(app, db)

    return app