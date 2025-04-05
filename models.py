from app import db

class User(db.Model):
    __tablename__ = 'users'  # Matches SQL table name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    money = db.Column(db.Integer)
    #lastName = db.Column(db.String(100), nullable=False)
    #type = db.Column(db.String(100), nullable=False)
    #contactInfo = db.Column(db.String(100), nullable=False)

class Income(db.Model):
    __tablename__ = 'income'  

    id = db.Column(db.Integer, primary_key=True)
    ownerId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    #TODO: set it up to just have a controlled variety of the type like salary, rental, etc. to clearly distinguish the table
    type = db.Column(db.String(100), nullable=False) 

class Assets(db.Model):
    __tablename__ = 'assets' 

    id = db.Column(db.Integer, primary_key=True)
    ownerId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) 
    type = db.Column(db.String(100), nullable=False)


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