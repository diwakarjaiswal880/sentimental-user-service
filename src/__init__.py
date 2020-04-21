from flask import Flask
import simplejson as json


def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    from src.views import bp

    app.register_blueprint(bp)

    @app.route("/health")
    def health():
        return json.dumps({"health": "alive"})

    return app
