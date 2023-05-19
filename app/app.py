from flask import Flask
from app.extensions import configuration, database, commands
from app.controllers.home_controller import app_bp
from app.controllers.router_controller import router_bp

app = Flask(__name__, template_folder='views/templates', static_folder='views/static')
configuration.init_app(app)
database.init_app(app)
commands.init_app(app)


app.register_blueprint(app_bp)
app.register_blueprint(router_bp)

if __name__ == '__main__':
    app.run()

"""


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/gerenciar/ip')
def gerenciar_ip():
    return render_template('ips.html')


@app.route('/gerenciar/usuarios')
def gerenciar_usuarios():
    return render_template('usuarios.html')


@app.route('/access')
def access_routes():
    # TODO lista de ips deveria ser lido de um arquivo txt, xls
    ips = ['192.168.0.101']
    # TODO não deixar usuário e senhas salvos em código
    username = 'admin'
    password = 'bkys182'

    for route in ips:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(route, username=username, password=password)
            # TODO comandos devem ser passados como parametros
            stdin, stdout, stderr = ssh.exec_command('user set roberto password=123123')
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

"""


