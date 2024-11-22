from flask import Flask

def create_app():
    """Función que devuelve la instancia de la aplicación flask"""

    app = Flask(__name__)

    @app.route('/')
    def map_app():
        return '<h1>Mi primera aplicación web map utilizando Flask</h1>'

    return app