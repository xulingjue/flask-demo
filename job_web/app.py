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
    from .handlers import front
    app.register_blueprint(front)


def register_apis(app):
    from .apis import user
    app.register_blueprint(user)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    register_extensions(app)
    register_blueprints(app)
    register_apis(app)
    return app


if __name__ == '__main__':
    app.run()
