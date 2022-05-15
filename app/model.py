from app import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

class User(db.Model,UserMixin):
    __tablename__ = 'users'

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255),unique=True,nullable=False)
    email=db.Column(db.String(255),unique=True,nullable=False)
    image_file=db.Column(db.String(255),nullable=False,default='default.jpg')
    password_hash=db.Column(db.String,nullable=False)

    @property
    def password(self):
        raise AttributeError("You can't read the password")

    @password.setter
    def password(self,password):
        self.password_hash=generate_password_hash(password)    

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)  

    
    def __repr__(self): 
        return f'{self.username}: {self.email}: {self.date_created}'      