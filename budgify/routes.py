from flask import flash, redirect, render_template, request, session, url_for
from budgify import app, db
from budgify.models import User, BudgetPlanner, Transaction
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
def home():
    return render_template("welcome.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
        if request.method == "POST":
            # Check if username already exists in DB
            existing_user = User.query.filter_by(
                username=request.form.get("username")
            ).first()

            if existing_user:
                flash("Username already exists, please choose another.")
                return redirect(url_for("register"))

            # Create new user
            new_user = User(
                username=request.form.get("username").lower(),
                password=generate_password_hash(request.form.get("password")),
            )
            db.session.add(new_user)
            db.session.commit()

            # Log in new user
            session["user"] = request.form.get("username")
            flash("Registration Successful!")

        return render_template("register.html")