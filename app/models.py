from .database import db
from geoalchemy2 import Geometry

class Estacion(db.Model):
    """Definición del modelo Estacion"""

    __tablename__ = 'estaciones' #nombre de la tabla

    codigo = db.Column(db.String(10), primary_key=True)
    nombre = db.Column(db.String(400)) 
    latitud = db.Column(db.Float)
    longitud = db.Column(db.Float)
    geom = db.Column(Geometry('POINT', srid=4326))
    ubicacion = db.Column(db.String(2000)) 
    altitud = db.Column(db.Float)

    datos = db.relationship('Dato', back_populates='estacion', lazy='dynamic')

    def __repr__(self):
        return 'Estacion %r' % self.nombre
    

class Variable(db.Model):
    """Definición del modelo Variable"""

    __tablename__ = 'variables' #nombre de la tabla

    codigo = db.Column(db.String(10), primary_key=True)
    variable = db.Column(db.String(500))
    unidad = db.Column(db.String(30))
    decimales = db.Column(db.Integer)

    datos = db.relationship('Dato', back_populates='variable', lazy='dynamic')

    def __repr__(self):
        return 'Variable: %r' % self.variable


class Dato(db.Model):
    """Definición del modelo Dato"""

    __tablename__ = 'datos' #nombre de la tabla

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha_lectura = db.Column(db.DateTime)
    valor_lectura = db.Column(db.Float)

    codigo_estacion = db.Column(db.String(10), db.ForeignKey('estaciones.codigo'), nullable=False)
    codigo_variable = db.Column(db.String(10), db.ForeignKey('variables.codigo'), nullable=False)

    estacion = db.relationship('Estacion', back_populates='datos')
    variable = db.relationship('Variable', back_populates='datos')

    def __repr__(self):
        return 'Valor: %r' % self.valor_lectura 