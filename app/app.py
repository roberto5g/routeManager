from flask import Flask
from app.extensions import configuration, database, commands, login
from app.controllers.home_controller import app_bp
from app.controllers.router_controller import router_bp
from app.controllers.user_controller import user_bp
from app.controllers.login_controller import login_bp
from app.controllers.log_controller import log_bp


app = Flask(__name__, template_folder='views/templates', static_folder='views/static')

configuration.init_app(app)
database.init_app(app)
commands.init_app(app)
login.init_app(app)


app.register_blueprint(login_bp)
app.register_blueprint(app_bp)
app.register_blueprint(router_bp)
app.register_blueprint(user_bp)
app.register_blueprint(log_bp)

if __name__ == '__main__':
    app.run()


