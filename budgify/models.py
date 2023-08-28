from budgify import db


class User(db.Model):
    # Schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    budget_planners = db.relationship(
        'BudgetPlanner', backref='user', cascade="all, delete", lazy=True)

    def __repr__(self):
        return f"User: {self.username}"


class BudgetPlanner(db.Model):
    # Schema for the BudgetPlanner model
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete='CASCADE'), nullable=False)
    transactions = db.relationship(
        'Transaction', backref='budget_planner',
        cascade="all, delete", lazy=True)

    def __repr__(self):
        return (
            f"Budget Planner Id: {self.id}, "
            f"Name: {self.name}, "
            f"User Id: {self.user_id}"
            )


class Transaction(db.Model):
    # Schema for the Transactions model
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    day_of_month = db.Column(db.Integer, nullable=False)
    transaction_type = db.Column(db.String(50), nullable=False)
    budget_planner_id = db.Column(db.Integer, db.ForeignKey(
        'budget_planner.id', ondelete='CASCADE'), nullable=False)

    def __repr__(self):
        return (
            f"Transaction ID: {self.id},"
            f"Transaction: {self.description}, "
            f"Amount: {self.amount}, "
            f"Day of Month: {self.day_of_month}, "
            f"Transaction Type: {self.transaction_type}, "
            f"Budget Planner ID: {self.budget_planner_id}"
        )
