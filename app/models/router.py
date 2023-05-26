from app.extensions.database import db


class Router(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(15), unique=True, nullable=False)

    def __init__(self, address):
        self.address = address

    def to_dict(self):
        return {
            'id': self.id,
            'address': self.address,
        }


