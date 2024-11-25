import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://josep:ZznZApfzHKQBDiMg16mp2hHgNM2l0mlC@dpg-ct055b56l47c7385mqh0-a.oregon-postgres.render.com/paw2'
    #SQLALCHEMY_DATABASE_URI = 'postgresql://josep:ZznZApfzHKQBDiMg16mp2hHgNM2l0mlC@dpg-ct055b56l47c7385mqh0-a/paw2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
