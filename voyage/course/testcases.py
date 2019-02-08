# -*- coding: utf-8 -*-

"""
This file is part of voyage.
 __file__ : testcases.py
"""

__author__ = 'Sri Pandi, Satheesh Rathinakumar'

# Python Default Modules

import unittest

from flask_restful import Api

from manage import init_app, db
from resources.sailing import SailingList
from resources.ship import ShipList


class CourseTestCase(unittest.TestCase):
    """This class represents the Course test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = init_app(conf_name="testing")
        self.client = self.app.test_client
        db.init_app(self.app)
        self.imo = 9247455

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

        api = Api(self.app)
        api.add_resource(ShipList, '/api/ships')
        api.add_resource(SailingList, '/api/positions/<int:imo>')

    def test_api_can_get_all_ships(self):
        """Test API can get a ships (GET request)."""

        res = self.client().get('/api/ships')
        print(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertIn('Ships', str(res.data))

    def test_api_can_get_all_positions(self):
        """Test API can get a all positions (GET request)."""

        res = self.client().get('/api/positions/{}'.format(self.imo))
        print(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertIn('Positions', str(res.data))

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
