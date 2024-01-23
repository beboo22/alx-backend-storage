#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """


def update_topics(mongo_collection, name, topics):
    """ Inserts a new document in a collection based on kwargs """
    nname = {"name": name}
    ntopics = {"$set": {"topics": topics}}
    x = mongo_collection.update_many(nname, ntopics)
