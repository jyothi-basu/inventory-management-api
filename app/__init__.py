from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

from app import routes
from app.auth import auth_bp

app.register_blueprint(auth_bp)
