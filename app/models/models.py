from datetime import datetime

from app import db


class ItemType(db.Model):
    __table_name__ = 'Item_Type'
    id = db.Column(db.Integer, primary_key=True, name='Item_Type_ID')
    item_type = db.Column(db.String(100), nullable=False)


class Item(db.Model):
    __table_name__ = 'Item'
    id = db.Column(db.Integer, primary_key=True, name='Item_ID')
    item_type_id = db.Column(db.Integer, db.ForeignKey(ItemType.id), nullable=False, name='Type_ID')
    item_type = db.relationship('ItemType')
    title = db.Column(db.Text, nullable=False, name='Title')
    in_possession = db.Column(db.Boolean, default=True, name='In_Possession')
    date_added = db.Column(db.Date, default=datetime.today().date(), name='Date_Added')
    date_removed = db.Column(db.Date, default=None, nullable=True, name='Date_Removed')
