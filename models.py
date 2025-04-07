from extensions import db
from datetime import datetime

#THIS ALREADY MATCHES WHAT THE SCHEMA IS AS OF 04-05

class User(db.Model):
    __tablename__ = 'users'  # Matches SQL table name

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    contactInfo = db.Column(db.String(100), nullable=False)
    
    
    
class Advisor(db.Model):
    __tablename__ = 'advisors'  # Matches SQL table name

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    contactInfo = db.Column(db.String(100), nullable=False)
    authId = db.Column(db.String(100), nullable=False)



class Income(db.Model):
    __tablename__ = 'income'  

    id = db.Column(db.Integer, primary_key=True)
    ownerId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    incomeType = db.Column(db.String(20), nullable=False)
    
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
    liabilityType = db.Column(db.String(50), nullable=False)
    amountOwed = db.Column(db.Integer, nullable=False)

class Blog(db.Model):
    __tablename__ = 'blog' 

    blogId = db.Column(db.Integer, primary_key=True)
    authorId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) 
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(500), nullable=False)
    tag = db.Column(db.String(100), nullable=False)
    author = db.relationship('User', backref='blogs')
    
    comments = db.relationship(
        'Comment',
        backref='blog',
        lazy=True,
        primaryjoin="Blog.blogId == Comment.blogId"
    )

    
class Comment(db.Model):
    __tablename__ = 'comments'
    
    commentId = db.Column(db.Integer, primary_key=True)
    blogId = db.Column(db.Integer, db.ForeignKey('blog.blogId'), nullable=False) 
    authorID = db.Column(db.Integer, db.ForeignKey('advisors.id'), nullable=False) 
    text = db.Column(db.String(500), nullable=False)



class Analysis(db.Model):
    __tablename__ = 'analysis'
    
    ownerId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, primary_key=True) 
    totalIncome = db.Column(db.Integer, nullable=False)
    totalAssets = db.Column(db.Integer, nullable=False)
    totalLiabilities = db.Column(db.Integer, nullable=False)


    
