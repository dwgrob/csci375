from flask import Flask, jsonify, request, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI
import os

#### DONT USE THESE VARIABLE NAMES #####:



# Configuration


db = SQLAlchemy()


def init():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.secret_key = 'Trash_Panda' 
    
    from pages import pages_bp
    from api import api_bp
    app.register_blueprint(pages_bp)
    app.register_blueprint(api_bp)
    
    with app.app_context():
        from models import User, Income, Assets, Liabilities, Blog 
        db.create_all()  # Ensure tables are created

    return app


if __name__ == '__main__':
    app = init()
    app.run(debug=True)