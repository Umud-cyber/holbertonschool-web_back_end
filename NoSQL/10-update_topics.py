#!/usr/bin/env python3
"""
this module defines a function that updates topics of a school document.
"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name.

    args:
        mongo_collection: the pymongo collection object.
        name (str): the name of the school to update.
        topics (list of str): the list of topics approached in the school.
    """
    # it uses update_many because there might be multiple documents
    # with the same school name, and we want to update all of them.
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
