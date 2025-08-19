from flask import Blueprint, render_template

route_dp = Blueprint('routes', __name__, template_folder="templates")
from . import user_routes