#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """


def schools_by_topic(mongo_collection, topic):
    """ Inserts a new document in a collection based on kwargs """
    x = mongo_collection.find({"topics": topics})
    return list(x)
