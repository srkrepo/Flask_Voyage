# -*- coding: utf-8 -*-

"""
This file is part of voyage.
 __file__ : config.py
"""

__author__ = 'Sri Pandi, Satheesh Rathinakumar'

# Python Default Modules
import os


class BaseConfig:
    """
    . Base class
    """

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')


class TestingConfig(BaseConfig):
    """
    . Test class
    """

    SECRET_KEY = '@HappySailing@'

    DB_NAME = 'voyage'
    DB_USER = 'postgres'
    DB_PASS = 'postgres'
    DB_SERVICE = 'localhost'
    DB_PORT = 5432

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}'.format(DB_USER, DB_PASS, DB_SERVICE,
                                                                                 DB_PORT, DB_NAME)
    DEBUG = True
    TESTING = True


class DevelopmentConfig(BaseConfig):
    """
    . Dev class
    """

    DB_SERVICE = os.environ['DB_SERVICE']
    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['DB_USER']
    DB_PASS = os.environ['DB_PASS']
    DB_PORT = os.environ['DB_PORT']

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}'.format(DB_USER, DB_PASS, DB_SERVICE,
                                                                                 DB_PORT, DB_NAME)
    DEBUG = True


class ProductionConfig(BaseConfig):
    """
    . Prod class
    """

    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
