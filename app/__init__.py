from flask import Flask
from app.app import app

x = Flask(__name__)
x.register_blueprint(app)