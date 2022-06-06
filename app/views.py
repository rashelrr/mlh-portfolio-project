import os
from flask import Blueprint, render_template
from dotenv import load_dotenv
from app.information import info

load_dotenv()
views = Blueprint('views', __name__, template_folder='templates')

@views.route("/")
def index():
    return render_template('index.html', name = info['name'], 
                        university = info['university'], 
                        about = info['about_yourself'], 
                        about2 = info['about_yourself2'],
                        education = info['education'], 
                        education_names = info['education_names'],
                        education_gpa = info['education_gpa'],
                        education_grad = info['education_graduation'],
                        education_duration = info['education_duration'],
                        url=os.getenv("URL"))

@views.route("/hobbies")
def hobbies():
    return render_template('hobbies.html', url=os.getenv("URL"))

@views.route("/map")
def map():
    return render_template('map.html', url=os.getenv("URL"))
