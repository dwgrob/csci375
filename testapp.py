from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI
import os

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://csci375team6:3jjjrun@dolphin/csci375team6_povertycalculator'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define Models
class User(db.Model):
    __tablename__ = 'users'  # Matches SQL table name

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100), nullable=False)  # Match "firstName" casing
    incomes = db.relationship('Income', backref='owner', lazy=True)

class Income(db.Model):
    __tablename__ = 'income'  # Matches SQL table name

    id = db.Column(db.Integer, primary_key=True)
    income = db.Column(db.Float, nullable=False)
    liabilities = db.Column(db.Float, nullable=True)
    obligations = db.Column(db.Float, nullable=True)
    ownerId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Match "ownerId" casing

# Serve the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Secure API to fetch income data using POST
@app.route('/secure-income-data', methods=['POST'])
def get_income_data():
    data = request.json

    # Optional authentication check
    if 'auth_token' not in data or data['auth_token'] != "secure_token_123":
        return jsonify({"error": "Unauthorized access"}), 401

    # Query matching SQL structure
    results = db.session.query(
        Income.id.label("id"),
        User.firstName.label("firstName"),
        Income.income.label("income"),
        Income.liabilities.label("liabilities"),
        Income.obligations.label("obligations")
    ).join(User, Income.ownerId == User.id).all()

    # Convert results to JSON
    response = [{
        "id": row.id,
        "firstName": row.firstName,  # Matches SQL column name
        "income": row.income,
        "liabilities": row.liabilities,
        "obligations": row.obligations
    } for row in results]
    
    return jsonify(response)

# API to add income data (POST)
@app.route('/add-income', methods=['POST'])
def add_income():
    data = request.json

    # Validate required fields
    if not all(k in data for k in ('firstName', 'income', 'liabilities', 'obligations')):
        return jsonify({"error": "Missing required fields"}), 400

    # Check if user exists, if not create a new one
    user = User.query.filter_by(firstName=data['firstName']).first()
    if not user:
        user = User(firstName=data['firstName'])
        db.session.add(user)
        db.session.commit()

    # Create new income entry
    new_income = Income(
        income=data['income'],
        liabilities=data['liabilities'],
        obligations=data['obligations'],
        ownerId=user.id  # Matches "ownerId" column
    )
    db.session.add(new_income)
    db.session.commit()

    return jsonify({"message": "Income added successfully"}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure tables are created
    app.run(debug=True)
