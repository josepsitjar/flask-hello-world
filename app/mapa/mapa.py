from flask import Blueprint
from ..database import db 
from flask import Blueprint, render_template

mapa_bp = Blueprint("mapa", __name__, template_folder='templates')

@mapa_bp.route("/")
def home():
    return render_template('mapa/vista.html')