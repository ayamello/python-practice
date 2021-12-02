from flask import Flask
from app.configs import migration, database, env_configs
from app.routes.lead_blueprint import bp 

def create_app():
    app = Flask(__name__)

    env_configs.init_app(app)
    database.init_app(app)
    migration.init_app(app)

    app.register_blueprint(bp)

    return app
