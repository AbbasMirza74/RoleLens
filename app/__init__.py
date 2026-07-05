from flask import Flask
import os
def create_app():
    app = Flask(__name__)
    app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
    from app.routes.dashboard import dashboard_bp
    app.register_blueprint(dashboard_bp)
    return app
