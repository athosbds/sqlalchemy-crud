from flask import Flask
from . import route_dp
from .models import db
from secrets_db import USER_DATABASE, PASSWORD_DATABASE, NAME_DATABASE

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{USER_DATABASE}:{PASSWORD_DATABASE}@localhost/{NAME_DATABASE}"
    )
    app.register_blueprint(route_dp)
    db.init_app(app)
    return app
    