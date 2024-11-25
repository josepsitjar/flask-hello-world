from flask import Blueprint
from ..database import db 
from flask import Blueprint, render_template
from shapely_geojson import dumps, Feature, FeatureCollection
from geoalchemy2.shape import to_shape
from ..models import Estacion

mapa_bp = Blueprint("mapa", 
                    __name__, 
                    template_folder='templates',
                    static_folder='static',
                    url_prefix='/mapa'
                    )

@mapa_bp.route("/")
def home():
    return render_template('mapa/vista.html')


@mapa_bp.route("/estaciones")
def estaciones_geojson():
    """Función para crear un archivo GeoJson a partir de los datos del modelo Estacion"""

    estaciones = []
    for estacion in Estacion.query.all():
        geometry = estacion.geom
        feature = Feature(to_shape(geometry), properties={'key': 'value'})
        estaciones.append(feature)

    feature_collection = FeatureCollection(estaciones)
    geoJson = dumps(feature_collection)

    return geoJson