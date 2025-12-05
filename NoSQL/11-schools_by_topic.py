#!/usr/bin/env python3
"""
this module defines a function to find documents based on a list item.
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of schools having a specific topic.

    args:
        mongo_collection: the pymongo collection object.
        topic (str): the topic to search for.

    returns:
        list: A list of dictionaries (documents) matching the topic.
    """
    # in MongoDB, if you query { "field": value } and "field" is an array,
    # MongoDB automatically checks if 'value' exists ANYWHERE in that array.
    query = {"topics": topic}

    # it uses find() with the query and convert the cursor to a list.
    return list(mongo_collection.find(query))
