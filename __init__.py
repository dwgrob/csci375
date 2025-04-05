from flask import Flask
from config import SQLALCHEMY_DATABASE_URI
from .extensions import db
from .pages import pages_bp




def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    
    from flask_sqlalchemy import SQLAlchemy
    db.init_app(app)
    
    
    
    app.register_blueprint(pages_bp)
    
    return app