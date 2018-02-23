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
    in_possession = db.Column(db.Boolean, default=True, name='In_Possession')
    date_added = db.Column(db.Date, default=datetime.today().date(), name='Date_Added')
    date_removed = db.Column(db.Date, default=None, nullable=True, name='Date_Removed')


class Book(db.Model):
    __table_name__ = 'Book'
    book_id = db.Column(db.Integer, primary_key=True, name='Book_ID')
    item_id = db.Column(db.Integer, db.ForeignKey(Item.id), nullable=False, name='Item_ID')
    item = db.relationship('Item', backref=db.backref('book_item', lazy=True))


class Comic(db.Model):
    __table_name__ = 'Comic'
    comic_id = db.Column(db.Integer, primary_key=True, name='Comic_ID')
    item_id = db.Column(db.Integer, db.ForeignKey(Item.id), nullable=False, name='Item_ID')
    item = db.relationship('Item', backref=db.backref('comic_item', lazy=True))


class Music(db.Model):
    __table_name__ = 'Music'
    music_id = db.Column(db.Integer, primary_key=True, name='Music_ID')
    item_id = db.Column(db.Integer, db.ForeignKey(Item.id), nullable=False, name='Item_ID')
    item = db.relationship('Item', backref=db.backref('music_item', lazy=True))


class Movie(db.Model):
    __table_name__ = 'Movie'
    movie_id = db.Column(db.Integer, primary_key=True, name='Movie_ID')
    item_id = db.Column(db.Integer, db.ForeignKey(Item.id), nullable=False, name='Item_ID')
    item = db.relationship('Item', backref=db.backref('movie_item', lazy=True))


class VideoGame(db.Model):
    __table_name__ = 'Video_Game'
    video_game_id = db.Column(db.Integer, primary_key=True, name='Video_Game_ID')
    item_id = db.Column(db.Integer, db.ForeignKey(Item.id), nullable=False, name='Item_ID')
    item = db.relationship('Item', backref=db.backref('video_game_item', lazy=True))