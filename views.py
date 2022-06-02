from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    username = "Carlos Seda"
    about_me = '''I am a computer science student who 
                faithfully believes that technology is 
                very powerful and is important for 
                evolution. Developing, innovating and learning 
                is what I do daily. I like to be aware of new 
                technologies and everything new that technology 
                companies create every day.'''

    return render_template("index.html", name = username, about = about_me)

@views.route("hobbies")
def hobbies():
    return render_template("index.html")


