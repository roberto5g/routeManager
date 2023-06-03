from app.models.log import Log
from app.extensions.database import db


class LogRepository:

    @staticmethod
    def get_all():
        return Log.query.all()

    @staticmethod
    def create(user_app, user_router, ip_address, description):
        log = Log(user_app, user_router, ip_address, description)
        db.session.add(log)
        db.session.commit()
        return log
