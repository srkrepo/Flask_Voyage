# -*- coding: utf-8 -*-

"""
This file is part of voyage.
 __file__ : ship.py.py
"""

__author__ = 'Sri Pandi, Satheesh Rathinakumar'

# Python Default Modules

# from flask import request
from flask_restful import Resource

from models.sailing import SailingModel


class SailingList(Resource):
    """
    Class Sailing
    """

    def get(self, imo):
        """

        :param imo:
        :return:
        """

        ships = SailingModel.find_by_imo(imo)
        if ships:
            return {'Positions': [ship.json() for ship in ships]}
        return {'message': 'Data not found'}, 404
