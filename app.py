from flask import Flask
from config import SQLALCHEMY_DATABASE_URI
from extensions import db
from datetime import datetime
from pages import pages_bp



def create_app():
    app = Flask(__name__)
    app.secret_key = 'Trash_Panda'
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    
    db.init_app(app)
    
    
    
    
    app.register_blueprint(pages_bp)
    
    return app




if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)