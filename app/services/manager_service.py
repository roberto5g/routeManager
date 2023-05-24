import paramiko
import re

from app.services.router_service import RouterService

router_service = RouterService()


class ManagerService:
    def process_router_data(self, data):
        if data['list_address'] == "on":
            routes_response = router_service.get_all_routers()
            for router in routes_response:
                print(router['address'])
                self.access_routes(router['address'], data['username'], data['password'], data['command'])

        if data['ip_address'] is not None:
            ip_list = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', data['ip_address'])
            for route in ip_list:
                self.access_routes(route, data['username'], data['password'], data['command'])

    @staticmethod
    def access_routes(route, username, password, command):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(route, username=username, password=password)
            stdin, stdout, stderr = ssh.exec_command(command)
            output = stdout.read().decode('utf-8')
            print(output)
            ssh.close()
        except paramiko.AuthenticationException:
            print(f'Falha na autenticação para o IP {route}')
        except paramiko.SSHException as ssh_exception:
            print(f'Erro SSH para o IP {route}: {ssh_exception}')
        except Exception as e:
            print(f'Erro ao conectar ao IP {route}: {e}')

        return 'Acesso aos dispositivos MikroTik concluído!'
