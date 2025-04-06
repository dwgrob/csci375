from flask import Flask, jsonify, request, render_template, session, redirect, url_for, Blueprint
from extensions import db
from models import User

api_bp = Blueprint("api_bp", __name__)

"""
@api_bp.route('/register', methods=['POST'])
def register():
    # Handle registration
    firstName = request.form.get('firstName')
    lastName = request.form.get('lastName')
    #contact_info = request.form.get('contactInfo')
    #user_type = request.form.get('type')
    # Check if the user already exists
    existing_user = User.query.filter_by(firstName=firstName).first()
    if existing_user:
        return jsonify({"message": "User with this contact info already exists."}), 400

    # Create a new user
    new_user = User(
        firstName=firstName,
        lastName=lastName,
        #contactInfo=contact_info,
        #type=user_type
    )

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201



@api_bp.route('/create-blog', methods=['POST'])
def create_blog():
    #user_id = session.get('user_id')
    #if not user_id:
        #return jsonify({"message": "User not logged in"}), 401

    title = request.form.get('title')
    tag = request.form.get('tag')
    text = request.form.get('text')
    user_id = request.form.get('user_id')

    new_blog = Blog(title=title, tag=tag, text=text, authorId=user_id)
    db.session.add(new_blog)
    db.session.commit()

    return jsonify({"message": "Blog created successfully"}), 201
"""

"""
@api_bp.route('/secure-income-data', methods=['POST'])
def get_income_data():
    data = request.json

    # Query matching SQL structure
    results = db.session.query(
        Income.id.label("id"),
        User.firstName.label("firstName"),
        Income.ownerID.label("OwnerID"),
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
"""


"""
# API to add income data (POST)
@api_bp.route('/add-income', methods=['POST'])
def add_income():
    data = request.json

    # Validate required fields
    #if not all(k in data for k in ('firstName', 'income', 'liabilities', 'obligations')):
    #    return jsonify({"error": "Missing required fields"}), 400

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
    """