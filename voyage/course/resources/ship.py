# -*- coding: utf-8 -*-

"""
This file is part of voyage.
 __file__ : ship.py.py
"""

__author__ = 'Sri Pandi, Satheesh Rathinakumar'

# Python Default Modules

# from flask import request
from flask_restful import Resource

from models.ship import ShipModel

class ShipList(Resource):
    """
    Class Ship
    """

    @classmethod
    def get(cls):
        """

        :return:
        """

        ships = ShipModel.find_all()
        if ships:
            return {'Ships': [ship.json() for ship in ships]}, 200
        return {'message': 'Data not found'}, 404
