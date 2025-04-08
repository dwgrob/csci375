from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI
import os

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'  # Matches SQL table name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    money = db.Column(db.Integer)
    #lastName = db.Column(db.String(100), nullable=False)
    #type = db.Column(db.String(100), nullable=False)
    #contactInfo = db.Column(db.String(100), nullable=False)
    
    
    
    
    
    
    
    
########## PAGES ##########################################################    
# any function that return a webpage template    
    
    
@app.route('/')
def index():
    return render_template('test.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login
        name = request.form.get('name')  # Assume this field is used to identify the user
        user = User.query.filter_by(name=name).first()
        
        if user:
            # Successful login
            return jsonify({"message": f"Welcome back, {user.name}!"}), 200
        else:
            return jsonify({"message": "Invalid credentials, please try again."}), 400
    return render_template('login.html')



@app.route('/user')
def user():
    # This would be the dashboard or user page after login
    return "User Dashboard"


@app.route('/blog')
def blog():
    return render_template('blog.html')







############# DATA MANIPULATION################################
# any function that fucks with data but does not return a webpage







@app.route('/register', methods=['POST'])
def register():
    # Handle registration
    name = request.form.get('name')
    #last_name = request.form.get('lastName')
    #contact_info = request.form.get('contactInfo')
    #user_type = request.form.get('type')
    money = request.form.get('money')

    # Check if the user already exists
    existing_user = User.query.filter_by(name=name).first()
    if existing_user:
        return jsonify({"message": "User with this contact info already exists."}), 400

    # Create a new user
    new_user = User(
        name=name,
        #lastName=last_name,
        #contactInfo=contact_info,
        #type=user_type
        money=money
    )

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201










if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure tables are created
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
    