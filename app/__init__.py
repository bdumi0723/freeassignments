# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask            import Flask
from flask_bootstrap  import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo    import PyMongo
from flask_login      import LoginManager

app = Flask(__name__, static_url_path='/static')

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/freeassign_dev"

#Configuration of application, see configuration.py, choose one and uncomment.
#app.config.from_object('configuration.ProductionConfig')
app.config.from_object('app.configuration.DevelopmentConfig')
#app.config.from_object('configuration.TestingConfig')

bs = Bootstrap(app)  #flask-bootstrap
db = SQLAlchemy(app) #flask-sqlalchemy

from app import views, models
