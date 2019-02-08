# -*- coding: utf-8 -*-

"""
This file is part of voyage.
 __file__ : manage.py
"""

__author__ = 'Sri Pandi, Satheesh Rathinakumar'

# Python Default Modules

import os

from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_restful import Api
from flask_script import Manager

from db import db
# from models.ship import ShipModel
# from models.sailing import SailingModel
from config import app_config


def init_app(conf_name):
    """

    :param conf_name:
    :return:
    """

    app = Flask(__name__)
    print(app_config[conf_name])
    app.config.from_object(app_config[conf_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app


# App Initialization with Config
config_name = os.getenv('APP_SETTINGS')  # config_name = 'development'
app = init_app(config_name)

# DB Initialization
db.init_app(app)
db.create_all(app=app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from resources.index import Index
from resources.ping import Ping
from resources.ship import ShipList
from resources.sailing import SailingList

api = Api(app)
api.add_resource(Index, '/')
api.add_resource(Ping, '/ping')
api.add_resource(ShipList, '/api/ships')
api.add_resource(SailingList, '/api/positions/<int:imo>')

if __name__ == '__main__':
    manager.run()
