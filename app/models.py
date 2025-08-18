from flask_sqlalchemy import SQLAlchemy, session

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
print('works it.')

def create_user(name, email, age):
    new = User(name, email, age)
    db.session.add(new)
    db.session.commit()

def update_user(id, name=None, email=None, age=None):
    user_update = User.query.filter(User.id == id).first()
    if user_update:
        if name:
            user_update.name = name
        if email:
            user_update.email = email
        if age:
            user_update.age = age
        db.session.commit()
