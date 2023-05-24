from app.repositories.router_repository import RouterRepository


class RouterService:

    def __init__(self):
        self.router_repository = RouterRepository()

    def get_all_routers(self):
        routes_response = self.router_repository.get_all()
        routers_dict = [router.to_dict() for router in routes_response]
        return routers_dict

    def get_router(self, router_id):
        return self.router_repository.get_by_id(router_id)

    def get_router_address(self, address):
        return self.router_repository.get_by_address(address)

    def create_router(self, address):
        existing_router = self.get_router_address(address)
        if existing_router:
            return False
        return self.router_repository.create(address)

    def update_router(self, router_id, address):
        return self.router_repository.update(router_id, address)

    def delete_router(self, router_id):
        return self.router_repository.delete(router_id)

