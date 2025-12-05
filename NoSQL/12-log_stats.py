#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB
Database: logs, Collection: nginx
"""
from pymongo import MongoClient


def log_stats():
    """
    Provides some stats about Nginx logs stored in MongoDB.
    """
    # Connect to default MongoDB client
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # Select the database and collection
    db = client.logs
    collection = db.nginx

    # 1. Count total number of documents
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # 2. Display methods statistics
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    
    for method in methods:
        # Count documents for each specific method
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # 3. Count status checks (method=GET, path=/status)
    status_check_count = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    log_stats()
