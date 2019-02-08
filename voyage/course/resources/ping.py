# -*- coding: utf-8 -*-

"""
This file is part of voyage.
 __file__ : ping.py
"""

__author__ = 'Sri Pandi, Satheesh Rathinakumar'

from flask_restful import Resource


class Ping(Resource):
    """
    Class Ping
    """

    def get(self):
        """

        :return:
        """

        print("Call from Test - GET")
        return {'message': 'Happy Sailing'}, 200


    def post(self):
        """

        :return:
        """

        print("Call from Test - POST")
        return {'message': 'Happy Sailing'}, 200
