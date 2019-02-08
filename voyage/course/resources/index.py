# -*- coding: utf-8 -*-

"""
This file is part of voyage.
 __file__ : index.py
"""

__author__ = 'Sri Pandi, Satheesh Rathinakumar'

# from flask import request
from flask import render_template, make_response
from flask_restful import Resource


class Index(Resource):
    """
    Class Ping
    """

    def get(self):
        """

        :return:
        """

        print("Call from Index - GET")
        posts = ''

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html', posts=posts), 200, headers)

    def post(self):
        """

        :return:
        """

        print("Call from Test - POST")
        return {'message': 'Happy Sailing'}, 200
