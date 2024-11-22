from flask import Blueprint 

mapa_bp = Blueprint("mapa", __name__)

@mapa_bp.route("/")
def home():
    return '<h1>Mi primer blueprint</h1>'