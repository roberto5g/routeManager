from app.repositories.log_repository import LogRepository


class LogService:

    def __init__(self):
        self.log_repository = LogRepository()

    def get_all_logs(self):
        logs_response = self.log_repository.get_all()
        logs_dict = [log.to_dict() for log in logs_response]
        return logs_dict

    def create_log(self, user_app, user_router, ip_address, description):
        return self.log_repository.create(user_app, user_router, ip_address, description)

