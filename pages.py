from flask import Flask, jsonify, request, render_template, session, redirect, url_for, Blueprint
from extensions import db
from models import Blog, Income, Comment, Assets, Liabilities
from datetime import datetime
from models import User, Advisor
from testfunction import *

pages_bp = Blueprint('pages_bp', __name__)


@pages_bp.route('/')
def index():
    #if the user is already logged in, redirecyt to the home page
    if 'user_name' in session.keys():
        return redirect(url_for("pages_bp.home", NME=session['user_name']))
    else: # otherwise redirect back to the login page
        return redirect(url_for('pages_bp.login'))


@pages_bp.route('/home')
def home():
    return render_template('home.html', NME=session['user_name'])


@pages_bp.route('/income')
def income():
    return render_template('income.html')


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
            session['isAdvisor'] = False
            
            # For brody to see that python can be called, should print id to terminal
            # surrounded by new lines
            test(user.id)

            return jsonify({"message": f"Welcome back, {user.firstName}!"}), 200
        else:
            return jsonify({"message": "Invalid credentials, please try again."}), 400

    return render_template('login.html')



@pages_bp.route('/advisor-login', methods=['GET', 'POST'])
def advisor_login():
    if request.method == 'POST':
        # Handle login
        #contactInfo = request.form.get('contactInfo')
        authId = request.form.get('authId')
        # Check if the user exists
        user = Advisor.query.filter_by(authId=authId).first()
        #session['advisor_id'] = advisor.id
        if user:
            # Successful login
            session['user_id'] = user.id
            session['user_name'] = user.firstName
            session['isAdvisor'] = True
            return jsonify({"message": f"Welcome back, {user.firstName}!"}), 200
        else:
            return jsonify({"message": "Invalid credentials, please try again."}), 400

    return render_template('advisor-login.html')


#For advisee
@pages_bp.route('/register', methods=['POST'])
def register():
    # Handle registration
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    contact_info = request.form.get('contactInfo')

    # Check if the user already exists
    existing_user = User.query.filter_by(contactInfo=contact_info).first()
    if existing_user:
        return jsonify({"message": "User with this contact info already exists."}), 400

    # Create a new user
    new_user = User(
        firstName=first_name,
        lastName=last_name,
        contactInfo=contact_info
    )

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201


@pages_bp.route('/advisor-register', methods=['POST'])
def advisor_register():
    # Handle registration
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    contact_info = request.form.get('contactInfo')
    auth_Id = request.form.get('authId')
    # Check if the user already exists
    existing_user = Advisor.query.filter_by(authId=auth_Id).first()
    #session['advisor_id'] = existing_user.id
    if existing_user:
        return jsonify({"message": "User with this contact info already exists."}), 400

    # Create a new user
    new_advisor = Advisor(
        firstName=first_name,
        lastName=last_name,
        contactInfo=contact_info,
        authId=auth_Id
    )

    # Add the new user to the database
    db.session.add(new_advisor)
    db.session.commit()

    return jsonify({"message": "Advisor registered successfully!"}), 201

@pages_bp.route('/logoff')
def logoff():
    session.pop("user_id", None)
    session.pop("user_name", None)
    session.pop("isAdvisor", None)
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
        blogs = Blog.query.filter_by(tag=selected_tag).options(
            db.joinedload(Blog.comments), db.joinedload(Blog.author)
        ).all()
    else:
        blogs = Blog.query.options(
            db.joinedload(Blog.comments), db.joinedload(Blog.author)
        ).all()

    blog_list = []
    for blog in blogs:
        blog_list.append({
            "id": blog.blogId,
            "title": blog.title,
            "tag": blog.tag,
            "text": blog.text,
            "author": blog.author,
            "comments": blog.comments 
        })

    return render_template('blog.html', posts=blog_list)


@pages_bp.route('/comment-blog', methods=['POST'])
def add_comment():
    user_id = session.get('user_id')
    #advisor_id = session.get('advisor.id')

    advisor = Advisor.query.get(user_id)

    #if not advisor:
        #return jsonify({"message": "Unauthorized"}), 403  

    blog_id = request.form.get('blog_id')
    text = request.form.get('text')

    new_comment = Comment(blogId=blog_id, authorID=advisor.id, text=text)
    db.session.add(new_comment)
    db.session.commit() 

    blog_list = Blog.query.all()
    return render_template('blog.html', posts=blog_list)

@pages_bp.route('/add-income', methods=['POST'])
def add_income():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "User not logged in"}), 401

    amount = request.form.get('amount')
    income_type = request.form.get('incomeType')

    new_income = Income(
        ownerId=user_id,
        amount=amount,
        incomeType=income_type
    )
    
    db.session.add(new_income)
    db.session.commit()

    return jsonify({"message": "Income added successfully"}), 201

@pages_bp.route('/add-asset', methods=['POST'])
def add_asset():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "User not logged in"}), 401

    asset_type = request.form.get('assetType')
    asset_value = request.form.get('assetValue')
    purchase_date = request.form.get('purchaseDate')

    new_asset = Assets(
        ownerId=user_id,
        assetType=asset_type,
        assetValue=asset_value,
        purchaseDate=datetime.strptime(purchase_date, '%Y-%m-%d') if purchase_date else None
    )
    
    db.session.add(new_asset)
    db.session.commit()

    return jsonify({"message": "Asset added successfully"}), 201

@pages_bp.route('/add-liability', methods=['POST'])
def add_liability():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "User not logged in"}), 401

    liability_type = request.form.get('liabilityType')
    amount_owed = request.form.get('amountOwed')

    new_liability = Liabilities(
        ownerId=user_id,
        liabilityType=liability_type,
        amountOwed=amount_owed
    )
    
    db.session.add(new_liability)
    db.session.commit()

    return jsonify({"message": "Liability added successfully"}), 201

@pages_bp.route('/get-financial-data', methods=['GET'])
def get_financial_data():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "User not logged in"}), 401

    # Get all data for the user
    incomes = Income.query.filter_by(ownerId=user_id).all()
    assets = Assets.query.filter_by(ownerId=user_id).all()
    liabilities = Liabilities.query.filter_by(ownerId=user_id).all()

    response = {
        "incomes": [{
            "id": i.id,
            "amount": i.amount,
            "type": i.incomeType,
            "created": i.created.isoformat() if i.created else None
        } for i in incomes],
        "assets": [{
            "id": a.id,
            "type": a.assetType,
            "value": a.assetValue,
            "purchaseDate": a.purchaseDate.isoformat() if a.purchaseDate else None
        } for a in assets],
        "liabilities": [{
            "id": l.id,
            "type": l.liabilityType,
            "amountOwed": l.amountOwed,
            "created": l.created.isoformat() if l.created else None
        } for l in liabilities]
    }
    
    return jsonify(response)


@pages_bp.route('/analysis')
def analysis():
    return render_template('analysis.html')


#=========================================================











