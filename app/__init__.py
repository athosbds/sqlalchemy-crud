from flask import Flask
from .models import db
from secrets_db import USER_DATABASE, PASSWORD_DATABASE, NAME_DATABASE

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{USER_DATABASE}:{PASSWORD_DATABASE}@localhost/{NAME_DATABASE}"
    )
    db.init_app(app)
    from .routes import route_dp
    app.register_blueprint(route_dp)
    with app.app_context():
        db.create_all()
    return app
    