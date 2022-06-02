from flask import Flask
from app.views import views

app = Flask(__name__)
app.register_blueprint(views)