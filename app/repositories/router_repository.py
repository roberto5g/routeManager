from app.models.router import Router
from app.extensions.database import db


class RouterRepository:

    @staticmethod
    def get_all():
        return Router.query.all()

    @staticmethod
    def get_by_id(router_id):
        return Router.query.get(router_id)

    @staticmethod
    def create(address):
        router = Router(address)
        db.session.add(router)
        db.session.commit()
        return router

    def update(self, router_id, address):
        router = self.get_by_id(router_id)
        router.address = address
        db.session.commit()
        return router

    def delete(self, router_id):
        router = self.get_by_id(router_id)
        db.session.delete(router)
        db.session.commit()
