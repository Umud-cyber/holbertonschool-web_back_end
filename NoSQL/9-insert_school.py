#!/usr/bin/env python3
"""
this module defines a function that inserts a new document into a collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection based on kwargs.

    args:
        mongo_collection: the pymongo collection object.
        **kwargs: arbitrary keyword arguments to be inserted as the document.

    returns:
        the _id of the newly inserted document.
    """
    # kwargs is already a dictionary containing the arguments passed.
    # example: insert_school(col, name="UCSF") -> kwargs = {'name': 'UCSF'}

    # insert_one() takes a dictionary and inserts it.
    # it returns an InsertOneResult object.
    result = mongo_collection.insert_one(kwargs)

    # it extracts the unique ID assigned to the new document.
    return result.inserted_id
