from flask import Flask
from . import route_dp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(route_dp)