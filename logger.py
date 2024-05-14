import logging
from logging.handlers import RotatingFileHandler
from elasticsearch import Elasticsearch
from pythonjsonlogger import jsonlogger
from datetime import datetime
import os
from concurrent.futures import ThreadPoolExecutor

# Elasticsearch setup
username = 'elastic'
password = 'sIPZEIW4WEcuOjWRTUYA'
es = Elasticsearch(["http://localhost:9200"], http_auth=(username, password))

# Executor for asynchronous tasks
executor = ThreadPoolExecutor(max_workers=2)

def setup_logger(name, log_file, level=logging.INFO):
    """Set up a logger that outputs JSON formatted logs."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(level)
        logger.propagate = False  # Preventing log messages from propagating to the root logger

        # Ensuring the directory for the log file exists
        log_directory = os.path.dirname(log_file)
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        # Creating a file handler
        file_handler = RotatingFileHandler(log_file, maxBytes=10240, backupCount=10)
        formatter = jsonlogger.JsonFormatter(
            fmt='%(asctime)s %(levelname)s %(message)s',
            datefmt='%Y-%m-%dT%H:%M:%SZ',
            rename_fields={
                'levelname': 'level',
                'message': 'log_string'
            }
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

def async_log_to_elasticsearch(doc):
    """Function to perform asynchronous log writing to Elasticsearch."""
    es.index(index="logs", document=doc)

def log_to_elasticsearch(log_level, log_message, log_file):
    """Prepare log data and submit to asynchronous execution."""
    doc = {
        'level': log_level,
        'log_string': log_message,
        'timestamp': datetime.utcnow().isoformat() + "Z",
        'metadata': {
            'source': log_file
        }
    }
    executor.submit(async_log_to_elasticsearch, doc)
