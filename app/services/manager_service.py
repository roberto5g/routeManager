import paramiko
import re

from app.services.router_service import RouterService
from app.services.user_service import UserService
from app.services.log_service import LogService

router_service = RouterService()
user_service = UserService()
log_service = LogService()


class ManagerService:
    def process_router_data(self, data):
        if data['list_address'] == "on":
            routes_response = router_service.get_all_routers()
            for router in routes_response:
                self.access_routes(router['address'], data['username'], data['password'], data['command'])

        if data['ip_address'] is not None:
            ip_list = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', data['ip_address'])
            for route in ip_list:
                self.access_routes(route, data['username'], data['password'], data['command'])
        return 'Acesso aos dispositivos MikroTik concluído!'

    @staticmethod
    def access_routes(route, username, password, command):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(route, username=username, password=password, timeout=10)
            stdin, stdout, stderr = ssh.exec_command(command)
            output = stdout.read().decode('utf-8')
            log_service.create_log(user_service.logged_user(), username, route, command)
            print(command, output, user_service.logged_user())
            ssh.close()
        except paramiko.AuthenticationException:
            print(f'Falha na autenticação para o IP {route}')
        except paramiko.SSHException as ssh_exception:
            print(f'Erro SSH para o IP {route}: {ssh_exception}')
        except Exception as e:
            print(f'Erro ao conectar ao IP {route}: {e}')
