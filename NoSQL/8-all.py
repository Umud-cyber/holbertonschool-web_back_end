#!/usr/bin/env python3
"""
this module defines a function that lists all documents in a collection.
"""


def list_all(mongo_collection):
    """
    lists all documents in a MongoDB collection.

    args:
        mongo_collection: The pymongo collection object to query.

    returns:
        A list of documents (dictionaries), or an empty list if none found.
    """
    # The .find() method in PyMongo returns a Cursor object (an iterator).
    # We can convert this cursor directly into a list.
    # If the collection is empty, find() returns an empty cursor,
    # and list(cursor) becomes [].
    return list(mongo_collection.find())
