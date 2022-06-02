from flask import Flask, Blueprint, render_template

#views = Blueprint(__name__, "app")
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title="")

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')