from app.extensions.database import db
from datetime import datetime


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_app = db.Column(db.String(100), nullable=False)
    user_router = db.Column(db.String(100), nullable=False)
    ip_address = db.Column(db.String(15), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, user_app, user_router, ip_address, description):
        self.user_app = user_app
        self.user_router = user_router
        self.ip_address = ip_address
        self.description = description

    def to_dict(self):
        return {
            'id': self.id,
            'user_app': self.user_app,
            'user_router': self.user_router,
            'ip_address': self.ip_address,
            'description': self.description,
            'created_at': self.created_at,
        }
