from flask import Flask
from app.mapa import mapa 
from config import Config 
from .database import db 
    
def create_app(config_class=Config):
    """Función que devuelve la instancia de la aplicación flask"""

    app = Flask(__name__)

    # cargamos los parámetros de configuración
    app.config.from_object(config_class)

    # instanciamos la base de datos
    db.init_app(app)

    app.register_blueprint(mapa.mapa_bp)

    return app