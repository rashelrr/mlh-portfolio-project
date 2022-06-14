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
                        about2 = data['about_yourself2'],
                        education = data['education'], 
                        education_names = data['education_names'],
                        education_gpa = data['education_gpa'],
                        education_grad = data['education_graduation'],
                        education_duration = data['education_duration'],
                        job_titles = data['job_titles'],
                        company_names = data['company_names'],
                        start_dates = data['start_dates'],
                        end_dates = data['end_dates'],
                        locations = data['locations'],
                        responsibilities = data['responsibilities'],
                        url=os.getenv("URL"))

@app.route("/hobbies")
def hobbies():
    return render_template('hobbies.html',
                        name = data['name'],
                        images = data['images'],
                        hobbies = data['hobbies'],
                        descriptions = data['descriptions'],
                        url=os.getenv("URL"))

@app.route("/map")
def map():
    return render_template('map.html', name = data['name'], url=os.getenv("URL"))
