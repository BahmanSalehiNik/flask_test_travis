from db import db


class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(255))
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.store_name = name

    def json(self):
        return {'name': self.store_name, 'items': [item.json() for item in self.items]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(store_name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


