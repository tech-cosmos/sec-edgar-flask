import unittest
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

class TestDatabase(unittest.TestCase):

    def setUp(self):
        # Set up a test database and create a connection to it
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:shivoham@127.0.0.1:5432/sec'
        self.db = SQLAlchemy(self.app)
        self.app_context = self.app.app_context()
        self.app_context.push()
    
    def tearDown(self):
        # Pop the application context after the test is finished
        self.app_context.pop()

    def test_connection(self):
        # Test that we can connect to the database
        try:
            self.db.engine.execute("SELECT 1")
        except Exception as e:
            self.fail(f"Could not connect to the database: {e}")

if __name__ == '__main__':
    unittest.main()