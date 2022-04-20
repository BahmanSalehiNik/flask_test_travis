"""
BaseTest

This class should be the parent of all non-unit tests
it allows for instantiation of the database dynamically
and makes sure that it is a new, blank database each time.
"""

import unittest
from app import app
from db import db


class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/test'
        app.config['DEBUG'] = False
        app.config['PROPAGATE_EXCEPTIONS'] = True
        with app.app_context():
            db.init_app(app)

    def setUp(self) -> None:
        # Make sure database exists

        with app.app_context():
            db.create_all()


        # Get a test client
        self.app = app
        self.app_context = app.app_context

    def tearDown(self) -> None:
        # Database is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()


