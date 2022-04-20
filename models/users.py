from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kaba:ikeecode@localhost/flasko'
app.config['SECRET_KEY'] = "kfvbsdkfgsfgnkg(_çty( fdbdsd))"

# initialisation de la base de donnee
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#

class Address(db.Model):
    __tablename__ ='address'
    id       = db.Column(db.Integer, primary_key=True, nullable=False)
    street   = db.Column(db.String(200), nullable=False)
    suite    = db.Column(db.String(200), nullable=False)
    city     = db.Column(db.String(200), nullable=False)
    zipcode  = db.Column(db.String(200), nullable=False)
    lat      = db.Column(db.Float, nullable=False)
    lng      = db.Column(db.Float, nullable=False)

    users    = db.relationship('User', backref='address', cascade='all, delete-orphan')



class Company(db.Model):
    __tablename__ ='company'
    id          = db.Column(db.Integer, primary_key=True, nullable=False)
    name        = db.Column(db.String(200), nullable=False, unique=True)
    catchPhrase = db.Column(db.String(200), nullable=False)
    bs          = db.Column(db.String(200), nullable=False)

    users       = db.relationship('User', backref='company', cascade='all, delete-orphan')


class User(db.Model):
    __tablename__ ='users'
    id        = db.Column(db.Integer, primary_key=True, nullable=False)
    name      = db.Column(db.String(200), nullable=False)
    username  = db.Column(db.String(200), nullable=False)
    email     = db.Column(db.String(200), nullable=False, index=True)
    addressId = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    phone     = db.Column(db.Integer, nullable=False)
    website   = db.Column(db.String(200), nullable=False)
    companyId = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    password  = db.Column(db.String(200), nullable=True)
    todos     = db.relationship('Todo', backref='users', cascade='all, delete-orphan')



class Todo(db.Model):
    __tablename__ ='todos'
    userId    = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    id        = db.Column(db.Integer, primary_key=True, nullable=False)
    title     = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, nullable=False)

    def __rep__(self):
        return f"Todod(id:{self.id}, title:{self.title}, completed:{self.completed}, userId:{self.userId})"

class Album(db.Model):
    __tablename__ ='albums'
    userId    = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    id        = db.Column(db.Integer, primary_key=True, nullable=False)
    title     = db.Column(db.String(200), nullable=False)
    photos    = db.relationship('Photo', backref='albums', cascade='all, delete-orphan')

    def __rep__(self):
        return f"userId:{self.userId}, id:{self.id}, title:{self.title}"



class Photo(db.Model):
    __tablename__ ='photos'
    albumId      = db.Column(db.Integer, db.ForeignKey('albums.id'), nullable=False)
    id           = db.Column(db.Integer, primary_key=True, nullable=False)
    title        = db.Column(db.String(200), nullable=False)
    url          = db.Column(db.String(200), nullable=False)
    thumbnailUrl = db.Column(db.LargeBinary, nullable=False)

    def __rep__(self):
        return f"Photo(albumId:{self.albumId}, id:{self.id}, title:{self.title}, url:{self.url})"


class Post(db.Model):
    __tablename__ ='posts'
    userId    = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    id        = db.Column(db.Integer, primary_key=True, nullable=False)
    title     = db.Column(db.String(200), nullable=False)
    body      = db.Column(db.Text, nullable=False)
    comments  = db.relationship('Comment', backref='posts', cascade='all, delete-orphan')


    def __rep__(self):
        return f"userId:{self.userId}, id:{self.id}, title:{self.title}"


class Comment(db.Model):
    __tablename__ ='comments'
    postId = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    id     = db.Column(db.Integer, primary_key=True, nullable=False)
    name   = db.Column(db.String(200), nullable=False)
    email  = db.Column(db.String(200), nullable=False)
    body   = db.Column(db.Text, nullable=False)

    def __rep__(self):
        return f"postId:{self.postId}, id:{self.id}, name:{self.name}, email:{self.email}"
