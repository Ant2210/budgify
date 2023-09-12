"""This module contains all the routes for the Budgify application."""

from flask import flash, redirect, render_template, request, session, url_for
from budgify import app, db
from budgify.models import TransactionType, User, BudgetPlanner, Transaction
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
def home():
    """Check for a user sessions and redirect accordingly.

    If no user session redirect to the welcome page, otherwise redirect to
    the users budgets page.
    """
    if "user" in session:
        return redirect(url_for("budgets", username=session["user"]))

    return render_template("welcome.html", hide_navbar=True)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register a new user and log them in."""
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
        session["user"] = request.form.get("username").lower()
        flash("Registration successful, let's create your first budget!")
        return redirect(url_for("budgets", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log in an existing user."""
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
                flash("Welcome, {}!".format(
                    request.form.get("username")).title())
                return redirect(url_for("budgets", username=session["user"]))
            else:
                # Invalid password match
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    """Log out the current user."""
    # Remove the user from the session
    flash("You have been logged out, come back again soon!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/budgets/<username>")
def budgets(username):
    """Display all budgets associated with the user."""
    # Check if the user is logged in
    if "user" not in session:
        flash("Please log in to view this page.")
        return redirect(url_for("login"))

    # Check if the user has permission to access this page
    if session["user"] != username:
        flash("You do not have permission to access this page.")
        return redirect(url_for("budgets", username=session["user"]))

    # Retrieve the username from the User object
    user_id = User.query.filter_by(
        username=session["user"]).with_entities(User.id).first_or_404()[0]
    budgets = BudgetPlanner.query.filter_by(user_id=user_id).all()

    # Pass the username as a variable to the "budgets" template
    return render_template("budgets.html", username=username, budgets=budgets)


@app.route("/budget/<username>/<int:budget_id>", methods=["GET", "POST"])
def budget(username, budget_id):
    """Display a single budget and allow the user to add, edit and delete."""
    # Check if the user is logged in
    if "user" not in session:
        flash("Please log in to view this page.")
        return redirect(url_for("login"))

    # Check if the user has permission to access this page
    if session["user"] != username:
        flash("You do not have permission to access this page.")
        return redirect(url_for("budgets", username=session["user"]))

    # Retrieve the username from the User object and budget information from
    # the BudgetPlanner object
    budget = BudgetPlanner.query.get_or_404(budget_id)
    transaction_types = TransactionType.query.all()
    transactions = Transaction.query.filter_by(
        budget_planner_id=budget_id).all()

    # Check if the budget belongs to the user
    if budget.user.username != username:
        flash("You do not have permission to access this page.")
        return redirect(url_for("budgets", username=session["user"]))

    # Pass the username as a variable to the "add_budget" template
    return render_template(
        "budget.html",
        username=username,
        budget_id=budget_id,
        budget=budget,
        transaction_types=transaction_types,
        transactions=transactions
    )


@app.route("/add_budget", methods=["POST"])
def add_budget():
    """Add a new budget to the database."""
    budget_planner = BudgetPlanner(
        name=request.form.get("budget_name"),
        user_id=User.query.filter_by(
            username=session["user"]
        ).with_entities(User.id).first_or_404()[0]
    )
    db.session.add(budget_planner)
    db.session.commit()
    flash("Budget created successfully, lets add some transactions!")
    return redirect(
        url_for(
            "budget", username=session["user"], budget_id=budget_planner.id
        )
    )


@app.route("/rename_budget/<username>/<int:budget_id>", methods=["POST"])
def rename_budget(username, budget_id):
    """Rename an existing budget."""
    budget = BudgetPlanner.query.get_or_404(budget_id)

    # Check if the budget belongs to the user
    if budget.user.username != username:
        flash("You do not have permission to access this page.")
        return redirect(url_for("budgets", username=session["user"]))

    budget.name = request.form.get("budget_name")
    db.session.commit()
    flash("Budget renamed successfully.")
    return redirect(
        url_for("budget", username=session["user"], budget_id=budget.id)
    )


@app.route("/delete_budget/<username>/<int:budget_id>", methods=["POST"])
def delete_budget(username, budget_id):
    """Delete an existing budget."""
    budget = BudgetPlanner.query.get_or_404(budget_id)

    # Check if the budget belongs to the user
    if budget.user.username != username:
        flash("You do not have permission to access this page.")
        return redirect(url_for("budgets", username=session["user"]))

    db.session.delete(budget)
    db.session.commit()
    flash("Budget deleted successfully.")
    return redirect(url_for("budgets", username=session["user"]))


@app.route("/add_transaction/<username>/<int:budget_id>", methods=["POST"])
def add_transaction(username, budget_id):
    """Add a new transaction to database and link to an existing budget."""
    # Retrieve the budget associated with the budget_id
    budget = BudgetPlanner.query.get_or_404(budget_id)

    # Check if the budget belongs to the user
    if budget.user.username != username:
        flash("You do not have permission to access this page.")
        return redirect(url_for("budgets", username=session["user"]))

    # Create new transaction
    transaction = Transaction(
        description=request.form.get("transaction_description"),
        amount=request.form.get("transaction_amount"),
        day_of_month=int(request.form.get("transaction_day")),
        type_id=int(request.form.get("transaction_type")),
        budget_planner_id=budget_id
    )
    db.session.add(transaction)
    db.session.commit()
    flash("Transaction added successfully.")
    return redirect(
        url_for("budget", username=session["user"], budget_id=budget_id)
    )


@app.route(
    "/edit_transaction/<username>/<int:budget_id>/<int:transaction_id>",
    methods=["POST"]
)
def edit_transaction(username, budget_id, transaction_id):
    """Edit an existing transaction."""
    # Retrieve the budget associated with the budget_id
    budget = BudgetPlanner.query.get_or_404(budget_id)

    # Check if the budget belongs to the user
    if budget.user.username != username:
        flash("You do not have permission to access this page.")
        return redirect(url_for("budgets", username=session["user"]))

    # Retrieve the transaction associated with the transaction_id
    transaction = Transaction.query.get_or_404(transaction_id)

    # Update the transaction
    transaction.description = request.form.get("transaction_description")
    transaction.amount = request.form.get("transaction_amount")
    transaction.day_of_month = int(request.form.get("transaction_day"))
    transaction.type_id = int(request.form.get("transaction_type"))
    db.session.commit()
    flash("Transaction updated successfully.")
    return redirect(
        url_for("budget", username=session["user"], budget_id=budget_id)
    )


@app.route(
    "/delete_transaction/<username>/<int:budget_id>/<int:transaction_id>",
    methods=["POST"]
)
def delete_transaction(username, budget_id, transaction_id):
    """Delete an existing transaction."""
    # Retrieve the transaction associated with the transaction_id
    transaction = Transaction.query.get_or_404(transaction_id)

    # Check if the budget belongs to the user
    if transaction.budget_planner.user.username != username:
        flash("You do not have permission to access this page.")
        return redirect(url_for("budgets", username=session["user"]))

    db.session.delete(transaction)
    db.session.commit()
    flash("Transaction deleted successfully.")
    return redirect(
        url_for("budget", username=session["user"], budget_id=budget_id)
    )


@app.route("/profile/<username>")
def profile(username):
    """Display the users profile page."""
    # Check if the user is logged in
    if "user" not in session:
        flash("Please log in to view this page.")
        return redirect(url_for("login"))

    # Check if the user has permission to access this page
    if session["user"] != username:
        flash("You do not have permission to access this page.")
        return redirect(url_for("budgets", username=session["user"]))

    # Pass the username as a variable to the "profile" template
    return render_template("profile.html", username=username)


@app.route("/change_password/<username>", methods=["POST"])
def change_password(username):
    """Change the users password."""
    # Check if the user is logged in
    if "user" not in session:
        flash("Please log in to view this page.")
        return redirect(url_for("login"))

    # Check if the user has permission to access this page
    if session["user"] != username:
        flash("You do not have permission to access this page.")
        return redirect(url_for("budgets", username=session["user"]))

    # Retrieve the user associated with the username
    user = User.query.filter_by(username=username).first_or_404()

    # Check if the old password matches
    if not check_password_hash(
        user.password, request.form.get("current-password")
    ):
        flash("Incorrect password, your password has not been updated.")
        return redirect(url_for("profile", username=username))

    # Update the password
    user.password = generate_password_hash(request.form.get("password"))
    db.session.commit()
    flash("Password updated successfully.")
    return redirect(url_for("profile", username=username))


@app.route("/delete_account/<username>", methods=["POST"])
def delete_account(username):
    """Delete the users account."""
    # Check if the user is logged in
    if "user" not in session:
        flash("Please log in to view this page.")
        return redirect(url_for("login"))

    # Check if the user has permission to access this page
    if session["user"] != username:
        flash("You do not have permission to access this page.")
        return redirect(url_for("profile", username=session["user"]))

    # Retrieve the user associated with the username
    user = User.query.filter_by(username=username).first_or_404()

    # Check if the old password matches
    if not check_password_hash(
        user.password, request.form.get("delete-account-password")
    ):
        flash("Incorrect password, your account has not been deleted.")
        return redirect(url_for("profile", username=username))

    # Delete the user
    db.session.delete(user)
    db.session.commit()
    session.pop("user")
    flash("Account deleted successfully, we're sorry to see you go.")
    return redirect(url_for("home"))


@app.errorhandler(404)
def page_not_found(e):
    """Display a custom 404 page.

    Solution found here https://shorturl.at/HJLTZ
    """
    return render_template("404.html"), 404
