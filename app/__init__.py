from flask import Flask

app = Flask(__name__)

from app import routes
from app.auth import auth_bp

app.register_blueprint(auth_bp)