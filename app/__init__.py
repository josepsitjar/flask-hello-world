from flask import Flask
from app.mapa import mapa 
from config import Config 
from .database import db 
from flask_bootstrap import Bootstrap
    
bootstrap = Bootstrap()

def create_app(config_class=Config):
    """Función que devuelve la instancia de la aplicación flask"""

    app = Flask(__name__, static_folder=None)

    # añadir bootstrap a la aplicación
    bootstrap.init_app(app)

    # cargamos los parámetros de configuración
    app.config.from_object(config_class)

    # instanciamos la base de datos
    db.init_app(app)

    app.register_blueprint(mapa.mapa_bp)

    return app