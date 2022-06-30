import os
import json
from flask import Blueprint, render_template
from dotenv import load_dotenv

load_dotenv()
app = Blueprint('app', __name__, template_folder='templates')

f = open ('app/data.json', "r")
data = json.loads(f.read())

@app.route("/")
def index():
    return render_template('index.html', name = data['name'], 
                        university = data['university'], 
                        about = data['about_yourself'], 
                        education = data['education'], 
                        experiences = data['experiences'],
                        url=os.getenv("URL"))

@app.route("/hobbies")
def hobbies():
    return render_template('hobbies.html', name = data['name'], 
                        hobbies = data['hobbies'],
                        url=os.getenv("URL"))
