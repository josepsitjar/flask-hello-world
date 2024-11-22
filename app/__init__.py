from flask import Flask
from app.mapa import mapa 

def create_app():
    """Función que devuelve la instancia de la aplicación flask"""

    app = Flask(__name__)

    app.register_blueprint(mapa.mapa_bp)

    return app