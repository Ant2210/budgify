from budgify import routes
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env


# Create an instance of Flask and store it in a variable called app
# Set the path to the static folder in order to serve the robots.txt file, code found here https://shorturl.at/nwFR5
app = Flask(__name__, static_folder='static', static_url_path='')
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)
