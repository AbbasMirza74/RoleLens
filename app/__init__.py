from flask import Flask
import os
def create_app():
    app = Flask(__name__)
    app.config["UPLOAD_FOLDER"] = os.path.join(app.root_path, "uploads")
    app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
    from app.routes.dashboard import dashboard_bp
    app.register_blueprint(dashboard_bp)
    return app