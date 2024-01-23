#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """
from pymongo import MongoClient


def Print_Nginx(nginx_collection):
    '''Provides some stats about Nginx logs stored in MongoDB.'''
    Nlog = nginx_collection.count_documents({})
    print("{} logs".format(Nlog))
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for m in method:
        methods = len(list(nginx_collection.find({'method': m})))
        print("\tmethod {}: {}".format(m, methods))
    status_check = len(list(nginx_collection.find({
        'method': "GET", 'path': '/status'})))
    print("{} status check".format(status_check))
    IPs = nginx_collection.aggregation([
        {
            '$group': {'_id':"ip"}
        },
        {
            '$limit': 10
        }
    ])
    print("IPs:")
    for Ip in IPs:
        print("\t{}:{}".format(Ip['_id']))

def run():
    '''Provides some stats about Nginx logs stored in MongoDB.'''
    client = MongoClient('mongodb://127.0.0.1:27017')
    Print_Nginx(client.logs.nginx)


if __name__ == '__main__':
    run()
