from flask import Flask
from flask_migrate import Migrate
from application.models import db

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


def create_app():
    app.config.from_envvar('FLASK_DEMO_APPLICATION_SETTINGS')
    register_extensions(app)
    register_blueprints(app)
    register_apis(app)
    return app


if __name__ == '__main__':
    create_app()
    app.run()
