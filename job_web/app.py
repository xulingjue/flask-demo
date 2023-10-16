# import json
# from flask import jsonify
from flask import Flask
from flask_migrate import Migrate
from job_web.config import configs
from job_web.models import db

app = Flask(__name__)


def register_extensions(app):
    db.init_app(app)
    Migrate(app, db)
    return


def register_blueprints(app):
    from .handlers import front_handler
    app.register_blueprint(front_handler)


def register_apis(app):
    from .apis import user_api
    app.register_blueprint(user_api)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    register_extensions(app)
    register_blueprints(app)
    register_apis(app)
    return app


if __name__ == '__main__':
    app.run()
