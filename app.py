from datetime import datetime
import logging
from flask import Flask, jsonify, request

from logger import setup_logger, log_to_elasticsearch

# Initializing the Flask application
app = Flask(__name__)

# Initializing loggers for different parts of the application, each logging to a different file
api_logger = setup_logger('api_logger', './logs/api.log')
data_logger = setup_logger('data_logger', './logs/data.log')
user_logger = setup_logger('user_logger', './logs/user.log')
update_logger = setup_logger('update_logger', './logs/update.log')
delete_logger = setup_logger('delete_logger', './logs/delete.log')
error_logger = setup_logger('error_logger', './logs/error.log', level=logging.ERROR)
login_logger = setup_logger('login_logger', './logs/login.log')
logout_logger = setup_logger('logout_logger', './logs/logout.log')
connect_logger = setup_logger('connect_logger', './logs/connect.log')

@app.route('/')
def home():
    """Serve the home page which provides a welcome message."""
    return "Welcome to the Quality Log Control System!"

@app.route('/api/test', methods=['GET'])
def test_api():
    """Endpoint to test basic API connectivity and logging."""
    api_logger.info("Test API accessed", extra={'source': 'api.log'})
    log_to_elasticsearch('info', 'Test API accessed', 'api.log')
    return jsonify(message="Test API endpoint hit!")

@app.route('/api/data', methods=['POST'])
def data_api():
    """Endpoint to receive and log data submissions."""
    try:
        data = request.json
        data_logger.info(f"Data received: {data}", extra={'source': 'data.log'})
        log_to_elasticsearch('info', f"Data received: {data}", 'data.log')
        return jsonify(data), 200
    except Exception as e:
        error_logger.error(f"Error processing data: {e}", extra={'source': 'error.log'})
        log_to_elasticsearch('error', f"Error processing data: {e}", 'error.log')
        return jsonify({"error": "Error processing data"}), 500

@app.route('/api/connect', methods=['GET'])
def connect():
    """Endpoint to simulate and log connection attempts."""
    try:
        raise ConnectionError("Failed to connect to the database.")
    except ConnectionError as e:
        connect_logger.error(f"Connection error occurred: {e}", extra={'source': 'connect.log'})
        log_to_elasticsearch('error', f"Connection error occurred: {e}", 'connect.log')
        return jsonify({"error": "Failed to connect"}), 500

@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Endpoint to fetch and log user information requests."""
    user_logger.info(f"Fetching user with ID: {user_id}", extra={'source': 'user.log'})
    return jsonify({"user_id": user_id, "name": "John Doe"}), 200

@app.route('/api/update', methods=['PUT'])
def update_data():
    """Endpoint to handle data update requests."""
    try:
        data = request.json
        update_logger.info("Update request received with data: {}".format(data), extra={'source': 'update.log'})
        log_to_elasticsearch('info', "Update request received", 'update.log')
        return jsonify({"status": "updated"}), 200
    except Exception as e:
        error_logger.error(f"Failed to update data: {e}", extra={'source': 'error.log'})
        log_to_elasticsearch('error', f"Failed to update data: {e}", 'error.log')
        return jsonify({"error": "Update failed"}), 500

@app.route('/api/delete/<int:id>', methods=['DELETE'])
def delete_item(id):
    """Endpoint to handle data deletion requests."""
    delete_logger.info(f"Delete request for ID: {id}", extra={'source': 'delete.log'})
    log_to_elasticsearch('info', f"Delete request for ID: {id}", 'delete.log')
    return jsonify({"status": "deleted"}), 200

@app.route('/api/error', methods=['GET'])
def simulate_error():
    """Endpoint to simulate and log errors."""
    try:
        raise ValueError("This is a simulated error")
    except Exception as e:
        error_logger.error(f"Simulated error occurred: {e}", extra={'source': 'simulated_error.log'})
        log_to_elasticsearch('error', f"Simulated error occurred: {e}", 'simulated_error.log')
        return jsonify({"error": "Simulated error"}), 500

@app.route('/api/login', methods=['POST'])
def login():
    """Endpoint to log user login attempts."""
    credentials = request.json
    login_logger.info("Login attempt with username: {}".format(credentials.get('username')), extra={'source': 'login.log'})
    log_to_elasticsearch('info', "Login attempt", 'login.log')
    return jsonify({"status": "logged in"}), 200

@app.route('/api/logout', methods=['GET'])
def logout():
    """Endpoint to log user logout actions."""
    logout_logger.info("User logged out successfully", extra={'source': 'logout.log'})
    log_to_elasticsearch('info', "User logout", 'logout.log')
    return jsonify({"status": "logged out"}), 200

if __name__ == '__main__':
    app.run(debug=True)
