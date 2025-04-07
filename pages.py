from flask import Flask, jsonify, request, render_template, session, redirect, url_for, Blueprint
from extensions import db
from models import Blog, Income
from datetime import datetime
from models import User

pages_bp = Blueprint('pages_bp', __name__)


# redirect with variables example: 
#           return redirect(url_for("compare", gameID=game, oppid=opponent))





@pages_bp.route('/')
def index():
    if session['user_name']:
        return redirect(url_for("home", NME=session['user_name']))
    else: 
        return redirect(url_for("login"))


@pages_bp.route('/home')
def home():
    return render_template('home.html', NME=session['user_name'])


@pages_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login
        contactInfo = request.form.get('contactInfo') 
        user = User.query.filter_by(contactInfo=contactInfo).first()
        
        if user:
            # Successful login
            session['user_id'] = user.id
            session['user_name'] = user.firstName
            session['user_type'] = user.type
            return jsonify({"message": f"Welcome back, {user.firstName}!"}), 200
        else:
            return jsonify({"message": "Invalid credentials, please try again."}), 400

    return render_template('login.html')

@pages_bp.route('/register', methods=['POST'])
def register():
    # Handle registration
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    contact_info = request.form.get('contactInfo')
    user_type = request.form.get('type')

    # Check if the user already exists
    existing_user = User.query.filter_by(contactInfo=contact_info).first()
    if existing_user:
        return jsonify({"message": "User with this contact info already exists."}), 400

    # Create a new user
    new_user = User(
        firstName=first_name,
        lastName=last_name,
        contactInfo=contact_info,
        type=user_type
    )

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201

@pages_bp.route('/logoff')
def logoff():
    session.pop("user_id", None)
    return redirect(url_for("login"))


@pages_bp.route('/create-blog', methods=['POST'])
def create_blog():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "User not logged in"}), 401

    title = request.form.get('title')
    tag = request.form.get('tag')
    text = request.form.get('text')

    new_blog = Blog(title=title, tag=tag, text=text, authorId=user_id)
    db.session.add(new_blog)
    db.session.commit()

    return jsonify({"message": "Blog created successfully"}), 201


@pages_bp.route('/blog')
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
            "comment": blog.comment
        })
        
    return render_template('blog.html', posts=blog_list)

@pages_bp.route('/comment-blog', methods=['POST'])
def add_comment():
    user_id = session.get('user_id')
    user = User.query.get(user_id)
    if not user or user.type != 'Adviser':
        return jsonify({"message": "Unauthorized"}), 403  

    blog_id = request.form.get('blog_id')
    comment = request.form.get('comment')

    blog = Blog.query.get(blog_id)
    blog.comment = comment
    db.session.commit() 
    return jsonify({"message": "Comment saved successfully"}), 200 


# Secure API to fetch income data using POST
@pages_bp.route('/secure-income-data', methods=['POST'])
def get_income_data():
    user_id = session.get('user_id')
    user_name = session.get('user_name')
    if not user_id:
        return jsonify({"message": "User not logged in"}), 401

    # Query matching SQL structure
    results = db.session.query(
        Income.id.label("id"),
        User.firstName.label("user_name"),
        Income.ownerId.label("ownerID"),
        Income.income.label("income"),
        Income.salary.label("salary"),
        Income.rentalIncome.label("rentalIncome"),
        Income.businessIncome.label("businessIncome"),
        Income.investments.label("investments"),
        Income.otherSources.label("otherSources"),
        Income.liabilities.label("liabilities"),
        Income.obligations.label("obligations")
    ).join(User, Income.ownerId == user_id).all()

    # Convert results to JSON
    response = [{
        "id": row.id,
        "firstName": row.name,  
        "income": row.income,
        "salary": row.salary,
        "rentalIncome": row.rentalIncome,
        "businessIncome": row.businessIncome,
        "investments": row.investments,
        "otherSources": row.otherSources,
        "liabilities": row.liabilities,
        "obligations": row.obligations
    } for row in results]
    
    return jsonify(response)


# API to add income data (POST)
@pages_bp.route('/add-income', methods=['POST'])
def add_income():
    user_id = session.get('user_id')
    user_name = session.get('user_name')
    if not user_id:
        return jsonify({"message": "User not logged in"}), 401

    income = request.form.get('income')
    salary = request.form.get('salary')
    rentalIncome = request.form.get('rentalIncome')
    businessIncome = request.form.get('businessIncome')
    investments = request.form.get('investments')
    otherSources = request.form.get('otherSources')
    liabilities = request.form.get('liabilities')
    obligations = request.form.get('obligations')
    ownerId = user_id

    # Create new income entry
    new_income = Income(
        income=income,
        salary=salary,
        rentalIncome=rentalIncome,
        businessIncome=businessIncome,
        investments=investments,
        otherSources=otherSources,
        liabilities=liabilities,
        obligations=obligations,
        ownerId=user_id 
    )
    db.session.add(new_income)
    db.session.commit()

    return jsonify({"message": "Income added successfully"}), 201

@pages_bp.route('/analysis')
def analysis():
    return render_template('analysis.html')


#=========================================================











