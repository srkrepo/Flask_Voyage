# -*- coding: utf-8 -*-

"""
This file is part of voyage.
 __file__ : ship.py
"""

__author__ = 'Sri Pandi, Satheesh Rathinakumar'

# Python Default Modules
from db import db


class SailingModel(db.Model):
    """
    .   SailingModel
    """

    __tablename__ = 'sailing'

    id = db.Column(db.Integer, primary_key=True)
    imo = db.Column(db.Integer, db.ForeignKey('ship.imo'))
    date_at = db.Column(db.DateTime, nullable=False)
    longitude_at = db.Column(db.Float(precision=10))
    latitude_at = db.Column(db.Float(precision=10))

    ship = db.relationship('ShipModel')

    def __init__(self, imo, date_at, longitude_at, latitude_at):
        """

        :param imo:
        :param date_at:
        :param longitude_at:
        :param latitude_at:
        """

        self.imo = imo
        self.date_at = date_at
        self.longitude_at = longitude_at
        self.latitude_at = latitude_at

    def json(self):
        """

        :return:
        """

        return {
            'imo': self.imo,
            'date_at': self.date_at,
            'longitude_at': self.longitude_at,
            'latitude_at': self.latitude_at,
        }

    @classmethod
    def find_by_imo(cls, imo):
        """
        Get position by name.
        :param imo:
        :return:
        """
        return cls.query.filter_by(imo=imo).order_by(cls.date_at.desc()).all()

    # def save_to_db(self):
    #     db.session.add(self)
    #     db.session.commit()

    # def delete_from_db(self):
    #     db.session.delete(self)
    #     db.session.commit()
