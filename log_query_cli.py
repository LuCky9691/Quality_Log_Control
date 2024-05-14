from elasticsearch import Elasticsearch
import json

# Setting up Elasticsearch connection using basic_auth for authentication
es = Elasticsearch(
    ["http://localhost:9200"],
    basic_auth=('elastic', 'j1PTS_ZQKafxF+oPvq8N')
)

def search_logs(level=None, log_string=None, regex_pattern=None, start_time=None, end_time=None, source=None):
    """Search logs in Elasticsearch based on provided filters."""
    query_filters = []

    # Adding a term filter for log level
    if level:
        query_filters.append({'term': {'level.keyword': level}})

    # Adding a match phrase filter for exact text search in log strings
    if log_string:
        query_filters.append({'match_phrase': {'log_string': log_string}})

    # Adding a regexp filter for pattern matching in log strings
    if regex_pattern:
        query_filters.append({'regexp': {'log_string': regex_pattern}})

    # Adding a match filter for source file
    if source:
        query_filters.append({'match': {'metadata.source': source}})

    # Adding a range filter for timestamp
    if start_time and end_time:
        query_filters.append({
            'range': {
                'timestamp': {
                    'gte': start_time,
                    'lte': end_time,
                    'format': "strict_date_optional_time"
                }
            }
        })

    # Constructing the overall query using a boolean must to require all conditions to be met
    query = {
        'size': 100,
        'query': {
            'bool': {
                'must': query_filters
            }
        }
    }

    response = es.search(index="logs", body=query)
    return response


def pretty_print_result(result):
    """Pretty print the search result."""
    hits = result['hits']['hits']
    for hit in hits:
        print(json.dumps(hit['_source'], indent=4))

if __name__ == "__main__":
    # Executing sample queries
    print("Query 1: Find all logs with the level set to 'error'.")
    result = search_logs(level='error')
    pretty_print_result(result)
    
    print("\nQuery 2: Search for logs with the message containing 'Failed to connect'.")
    result = search_logs(log_string='Failed to connect')
    pretty_print_result(result)
    
    print("\nQuery 3: Filter logs between '2023-09-10T00:00:00Z' and '2023-09-15T23:59:59Z'.")
    result = search_logs(start_time='2023-09-10T00:00:00Z', end_time='2023-09-15T23:59:59Z')
    pretty_print_result(result)
    
    print("\nQuery 3: Filter logs containing the phrase Failed to connect between '2023-09-10T00:00:00Z' and '2023-09-15T23:59:59Z'.")
    # Example: Find error logs containing the phrase "Failed to connect" within a specific date range
    result = search_logs(
    level='error',
    log_string='Failed to connect',
    start_time='2023-09-10T00:00:00Z',
    end_time='2024-09-15T23:59:59Z'
)
    pretty_print_result(result)

    
    

