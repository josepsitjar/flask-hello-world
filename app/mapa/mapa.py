from flask import Blueprint 

mapa_bp = Blueprint("mapa", __name__)
from ..database import db 

@mapa_bp.route("/")
def home():
    return '<h1>Mi primer blueprint</h1>'

@mapa_bp.route("/inicializar_db")
def inicializar_db():
    try:
        db.create_all()
        return "La base de datos se ha creado correctamente.", 200
    except Exception as e: 
        return f"Ha ocurrido un error: {e}", 500