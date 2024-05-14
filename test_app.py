import unittest
from flask_testing import TestCase
from app import app

class FlaskTest(TestCase):
    """
    Defining a test case class for the Flask application by inheriting from TestCase.
    This class will contain methods to test different endpoints of the application.
    """

    def create_app(self):
        """
        Setting up the Flask application for testing. This method is called automatically
        by the Flask-Testing framework to configure the Flask app for testing.
        """
        app.config['TESTING'] = True  # Enable testing mode to handle exceptions and errors.
        return app

    def test_home(self):
        """
        Testing the home endpoint to ensure it returns a successful response and the correct welcome message.
        """
        response = self.client.get('/')  # Send a GET request to the home endpoint.
        self.assertEqual(response.status_code, 200)  # Assert that the response status code is 200.
        self.assertIn(b'Welcome to the Quality Log Control System!', response.data)  # Check if the welcome message is in the response.

    def test_test_api(self):
        """
        Testing the test_api endpoint to check if it responds successfully with the correct message.
        """
        response = self.client.get('/api/test')  # Send a GET request to the test_api endpoint.
        self.assertEqual(response.status_code, 200)  # Ensure the response status code is 200.
        self.assertIn(b'Test API endpoint hit!', response.data)  # Verify the correct message is returned.

    def test_error_api(self):
        """
        Testing the error API endpoint to ensure it handles errors correctly and returns an error response.
        """
        response = self.client.get('/api/error')  # Send a GET request to the error simulation endpoint.
        self.assertEqual(response.status_code, 500)  # Expect a 500 status code indicating an internal server error.
        self.assertIn(b'Simulated error', response.data)  # Confirm the error message appears in the response.

if __name__ == '__main__':
    unittest.main()  # Executing the tests when the script is run directly.
