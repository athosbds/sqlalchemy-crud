from flask import Blueprint, render_template

route_dp = Blueprint('routes', __name__, template_folder="templates", url_prefix='/users')
from . import user_routes