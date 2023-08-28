from flask import render_template
from budgify import app, db
from budgify.models import User, BudgetPlanner, Transaction


@app.route("/")
def home():
    return render_template("base.html")