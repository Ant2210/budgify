from flask import render_template
from budgify import app, db
from budgify.models import User, BudgetPlanner, Transaction


@app.route("/")
def home():
    return render_template("welcome.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")