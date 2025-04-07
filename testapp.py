from flask import Flask, jsonify, request, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI
import os

app = Flask(__name__)
app.secret_key = 'Trash_Panda' 

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Defining Models that need to match what we have on our tables in our database



###################################################################
########################## MODELS #################################
###################################################################


#TODO: needs to match the table from poverty calculator table
class User(db.Model):
    __tablename__ = 'users'  # Matches SQL table name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    money = db.Column(db.Integer)
    #lastName = db.Column(db.String(100), nullable=False)
    #type = db.Column(db.String(100), nullable=False)
    #contactInfo = db.Column(db.String(100), nullable=False)

#TODO: set it up to just have different tables of different type of income
class Income(db.Model):
    __tablename__ = 'income'  

    id = db.Column(db.Integer, primary_key=True)
    ownerId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    #TODO: set it up to just have a controlled variety of the type like salary, rental, etc. to clearly distinguish the table
    type = db.Column(db.String(100), nullable=False) 

#TODO: set it up to just have different tables of different types of assets
class Assets(db.Model):
    __tablename__ = 'assets' 

    id = db.Column(db.Integer, primary_key=True)
    ownerId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) 
    type = db.Column(db.String(100), nullable=False)
    
#TODO: set it up to just have different tables of different type of liabilities
class Liabilities(db.Model):
    __tablename__ = 'liabilities' 

    id = db.Column(db.Integer, primary_key=True)
    ownerId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) 
    type = db.Column(db.String(100), nullable=False)

class Blog(db.Model):
    __tablename__ = 'blog' 

    blogId = db.Column(db.Integer, primary_key=True)
    authorId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) 
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(100), nullable=False)
    tag = db.Column(db.String(100), nullable=False)
    author = db.relationship('User', backref='blogs')


############################################################################################
#====================================== PAGES =====================================================
############################################################################################

# Serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login
        name = request.form.get('name') 
        user = User.query.filter_by(name=name).first()
        
        if user:
            # Successful login
            return jsonify({"message": f"Welcome back, {user.name}!"}), 200
        else:
            return jsonify({"message": "Invalid credentials, please try again."}), 400
    #session['user_id'] = User.id
    #print(session['user_id'])
    return render_template('login.html')

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


############################################################################################
#====================================== PAGES =====================================================
############################################################################################


@app.route('/create-blog', methods=['POST'])
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


@app.route('/blog')
def get_blogs():
    selected_tag = request.args.get('tag')  
    
    if selected_tag:
        blogs = Blog.query.filter_by(tag=selected_tag).all()
    else:
        blogs = Blog.query.all()

    blog_list = []
    for blog in blogs:
        blog_list.append({
            "id": blog.blogId,
            "title": blog.title,
            "tag": blog.tag,
            "text": blog.text,
            "author": blog.author,
        })
        
    return render_template('blog.html', posts=blog_list)

############################################################################################
#====================================== API =====================================================
############################################################################################


@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

# Secure API to fetch income data using POST
@app.route('/secure-income-data', methods=['POST'])
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

# API to add income data (POST)
@app.route('/add-income', methods=['POST'])
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

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure tables are created
    app.run(debug=True)
