#!/usr/bin/env python3
"""
this module provides stats about Nginx logs stored in MongoDB.
it connects to the logs database and analyzes the nginx collection.
"""
from pymongo import MongoClient


def log_stats():
    """
    calculates and prints statistics about the Nginx logs.
    """
    # connect to the MongoDB server
    client = MongoClient('mongodb://127.0.0.1:27017')

    # select the database and collection
    nginx_collection = client.logs.nginx

    # get the total number of documents
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # calculate stats for specific HTTP methods
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        # count documents where the field 'method' matches the current method
        count = nginx_collection.count_documents({"method": method})
        # the requirement specifies a tabulation (\t) before the method name
        print(f"\tmethod {method}: {count}")

    # get the count of status checks
    # it filters for method="GET" AND path="/status"
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
