from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    db.init_app(app)

    from src.views import bp

    app.register_blueprint(bp)

    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
