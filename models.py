from extensions import db
from datetime import datetime

#THIS ALREADY MATCHES WHAT THE SCHEMA IS AS OF 04-05

class User(db.Model):
    __tablename__ = 'users'  # Matches SQL table name

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    contactInfo = db.Column(db.String(100))

class Income(db.Model):
    __tablename__ = 'income'  

    id = db.Column(db.Integer, primary_key=True)
    ownerId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    income = db.Column(db.Integer)
    salary = db.Column(db.Integer)
    rentalIncome = db.Column(db.Integer)
    businessIncome = db.Column(db.Integer)
    investments = db.Column(db.Integer)
    otherSources = db.Column(db.Integer)
    liabilities = db.Column(db.Integer)
    obligations = db.Column(db.Integer)

class Assets(db.Model):
    __tablename__ = 'assets' 

    id = db.Column(db.Integer, primary_key=True)
    ownerId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) 
    assetType = db.Column(db.String(50))
    assetValue = db.Column(db.Integer)
    purchaseDate = db.Column(db.DateTime)


class Liabilities(db.Model):
    __tablename__ = 'liabilities' 

    id = db.Column(db.Integer, primary_key=True)
    ownerId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) 
    liabilityType = db.Column(db.String(50))
    amountOwed = db.Column(db.Numeric(12, 6))
    apr = db.Column(db.Numeric(2, 2))

class Blog(db.Model):
    __tablename__ = 'blog' 

    blogId = db.Column(db.Integer, primary_key=True)
    authorId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) 
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(100), nullable=False)
    tag = db.Column(db.String(100), nullable=False)
    author = db.relationship('User', backref='blogs')