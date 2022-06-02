import os
from flask import Blueprint, render_template
from dotenv import load_dotenv

load_dotenv()
views = Blueprint('views', __name__, template_folder='templates')

@views.route("/")
def index():
    return render_template('index.html', url=os.getenv("URL"))
