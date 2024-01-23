#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """


def schools_by_topic(mongo_collection, topic):
    """ Inserts a new document in a collection based on kwargs """
    doc = {"topics": topic}
    result = mongo_collection.find(doc)
    return result
