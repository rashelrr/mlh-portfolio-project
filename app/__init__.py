from peewee import *
from flask import Flask
from app.app import app

x = Flask(__name__)
x.register_blueprint(app)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
                     user=os.getenv("MYSQL_USER"),
                     password=os.getenv("MYSQL_PASSWORD"),
                     host=os.getenv("MYSQL_HOST"),
                     port=3306
                    )

print(mydb)
