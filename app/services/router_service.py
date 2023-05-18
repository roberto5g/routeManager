from app.repositories.router_repository import RouterRepository


class RouterService:

    def __init__(self):
        self.router_repository = RouterRepository()

    def get_all_routers(self):
        return self.router_repository.get_all()

    def get_router(self, router_id):
        return self.router_repository.get_by_id(router_id)

    def create_router(self, address):
        return self.router_repository.create(address)

    def update_router(self, router_id, address):
        return self.router_repository.update(router_id, address)

    def delete_router(self, router_id):
        return self.router_repository.delete(router_id)

