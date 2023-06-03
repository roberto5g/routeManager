from app.extensions.database import db
from app.models.router import Router
from app.models.user import User
from app.models.log import Log


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_router_table():
    """Populate db with sample data"""
    data = [
        Router(
            address="192.168.0.1"),
        Router(
            address="192.168.0.2")
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return Router.query.all()


def populate_user_table():
    """Populate db with sample data"""
    data = [
        User(
            login="roberto.santos",
            password="123123"
        ),
        User(
            login="aldo.alex",
            password="123123"
        )
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return User.query.all()


def populate_log_table():
    """Populate db with sample data"""
    data = [
        Log(
            user_app="roberto",
            user_router="admin",
            ip_address="0.0.0.0",
            description="user print",
        )
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return Log.query.all()


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_router_table, populate_user_table, populate_log_table]:
        app.cli.add_command(app.cli.command()(command))
