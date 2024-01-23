#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """
from pymongo import MongoClient


def top_students(mongo_collection):
    """The correct method name for aggregation is aggregate, not aggregation"""
    std_values = mongo_collection.aggregate([
        {
            '$project': {
                '_id': 1,
                'name': 1,
                'averageScore': {
                    '$avg': '$topics.score'
                }
            }
        },
        {
            '$sort': {
                'averageScore': -1
            }
        }
    ])
    return std_values
