from flask import flash, redirect, render_template, request, session, url_for
from budgify import app, db
from budgify.models import User, BudgetPlanner, Transaction
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
def home():
    if "user" in session:
        return redirect(url_for("budgets"))
    
    return render_template("welcome.html", hide_navbar=True)


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
            flash("Registration Successful, let's create your first budget!")
            return redirect(url_for("budgets"))

        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if username already exists in DB
        existing_user = User.query.filter_by(
            username=request.form.get("username").lower()
        ).first()

        if existing_user:
            # Check if password matches
            if check_password_hash(
                existing_user.password, request.form.get("password")
            ):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}!".format(request.form.get("username")).title())
                return redirect(url_for("budgets"))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
            
        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
            
    return render_template("login.html")


@app.route("/logout")
def logout():
    # Remove the user from the session
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/budgets")
def budgets():
    return render_template("budgets.html")