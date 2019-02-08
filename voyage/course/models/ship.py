# -*- coding: utf-8 -*-

"""
This file is part of voyage.
 __file__ : ship.py
"""

__author__ = 'Sri Pandi, Satheesh Rathinakumar'

# Python Default Modules
from db import db


class ShipModel(db.Model):
    """
    .   ShipModel
    """

    __tablename__ = 'ship'

    id = db.Column(db.Integer)
    imo = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(25))

    sailing = db.relationship('SailingModel', lazy="dynamic")

    def __init__(self, imo, name):
        """

        :param imo:
        :param name:
        """

        self.imo = imo
        self.name = name

    def json(self):
        """

        :return:
        """

        return {
            'imo': self.imo,
            'name': self.name
        }

    @classmethod
    def find_all(cls):
        """

        :return:
        """

        return cls.query.order_by(cls.name).all()

    # @classmethod
    # def find_by_name(cls, name):
    #     return cls.query.filter_by(name=name).first()

    # def save_to_db(self):
    #     db.session.add(self)
    #     db.session.commit()

    # def delete_from_db(self):
    #     db.session.delete(self)
    #     db.session.commit()
