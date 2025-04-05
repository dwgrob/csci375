from flask import Flask, jsonify, request, render_template, session, redirect, url_for, Blueprint
from extensions import db
from models import User

pages_bp = Blueprint('pages_bp', __name__)


@pages_bp.route('/')
def index():
    return render_template('index.html')


@pages_bp.route('/login', methods=['GET', 'POST'])
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
        })
        
    return render_template('blog.html', posts=blog_list)


@pages_bp.route('/analysis')
def analysis():
    return render_template('analysis.html')


#=========================================================






@pages_bp.route('/register', methods=['POST'])
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




