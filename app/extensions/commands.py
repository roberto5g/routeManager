from app.extensions.database import db
from app.models.router import Router


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    data = [
        Router(
            address="192.168.0.1")
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return Router.query.all()


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))
