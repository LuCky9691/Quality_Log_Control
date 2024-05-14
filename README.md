### README.md for Log Control System

---

## Log Control System

The Log Control System is a Flask-based application that integrates with Elasticsearch to provide advanced logging solutions. This system includes multiple endpoints to simulate API behaviors, logs these interactions, and allows for complex querying of these logs via Elasticsearch.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- Flask
- Elasticsearch
- Python packages: `elasticsearch`, `flask`, `python-json-logger`

### Installation

#### Python Environment Setup

1. **Clone the repository** to your local machine:

```bash
git clone https://your-repository-url.git
cd quality_log_control
```

2. **Install the required Python packages**:

```bash
pip install Flask elasticsearch python-json-logger
```

If you prefer to install all dependencies at once from a `requirements.txt` file (recommended for maintaining consistent environments across all users), ensure your `requirements.txt` contains:

```
Flask
elasticsearch
python-json-logger
```

Then run the installation command:

```bash
pip install -r requirements.txt
```

#### Elasticsearch Setup

Elasticsearch is a highly scalable open-source full-text search and analytics engine. It allows you to store, search, and analyze big volumes of data quickly and in near real-time. It is generally used as the underlying engine/technology that powers applications with complex search features and requirements.

1. **Download and Install Elasticsearch**:

   You can download Elasticsearch from the [official Elastic website](https://www.elastic.co/downloads/elasticsearch). Choose the version that is compatible with your operating system.

2. **Start Elasticsearch**:

   After installation, you can run Elasticsearch on your local machine. On most systems, the default way to start Elasticsearch is through the command line:

   ```bash
   cd path/to/elasticsearch/
   ./bin/elasticsearch
   ```

   On Windows, you would use:

   ```bash
   cd path/to/elasticsearch/
   bin\elasticsearch.bat
   ```

   Ensure Elasticsearch is running by accessing [http://localhost:9200](http://localhost:9200) in your web browser or using a command line tool like `curl`:

   ```bash
   curl http://localhost:9200/
   ```

3. **Set Up Authentication**:

   For security, Elasticsearch uses authentication. The default username is `elastic`. To set or reset the password for the `elastic` user, use the `elasticsearch-reset-password` tool provided by Elasticsearch:

   ```bash
   bin/elasticsearch-reset-password -u elastic
   ```

   This command will prompt you to enter a new password and will confirm once the password is successfully changed. You'll use this username and password to configure the connection to Elasticsearch from your application.

### Running the Application

Navigate to the project directory and run the Flask application:

```bash
python app.py
```

This will start your Flask server, and the application will begin logging as per the endpoints defined.

---
### Using the Log Query CLI

To use the CLI for querying logs, run:

```bash
python log_query_cli.py
```

#### Example Queries

- **Find Error Logs**:

  ```bash
  python log_query_cli.py --level error
  ```

- **Search for a specific message**:

  ```bash
  python log_query_cli.py --log_string "Failed to connect"
  ```

- **Filter by date range**:

  ```bash
  python log_query_cli.py --start_time "2023-09-10T00:00:00Z" --end_time "2023-09-15T23:59:59Z"
  ```

Automated Testing with Python (using unittest)
unittest is a built-in Python module used to implement unit tests. It provides a rich set of tools for constructing and running tests, ensuring that your application behaves as expected. To enhance the testing capabilities for Flask applications, the Flask-Testing extension can be used.

Set Up a Testing Environment
Install Flask-Testing:

This extension provides additional testing capabilities beyond what's provided by unittest. Install it using pip:

pip install Flask-Testing

### Configuration

Ensure that the Elasticsearch credentials (username and password) are correctly set in your application configuration or passed appropriately when initializing the Elasticsearch client in your code. This is essential for avoiding authentication errors and ensuring smooth operation of your log system.

---

By using these steps to set up authentication, including how to reset the password, this README helps ensure that users can successfully authenticate and interact with Elasticsearch in their development environment.
