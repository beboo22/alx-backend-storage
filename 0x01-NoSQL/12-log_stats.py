#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """
from pymongo import MongoClient


def Print_Nginx(nginx_collection):
    Nlog = nginx_collection.count_documents({})
    print("{} logs".format(Nlog))
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:\n")
    for m in method:
        methods = len(list(nginx_collection.find({'method': m})))
        print("\tmethod {}: {}".format(m, methods))
    status_check = len(list(nginx_collection.find({
        'method': "GET", 'path': '/status'})))
    print("{} status check".format(status_check))


def run():
    '''Provides some stats about Nginx logs stored in MongoDB.'''
    client = MongoClient('mongodb://127.0.0.1:27017')
    Print_Nginx(client.logs.nginx)


if __name__ == '__main__':
    run()
# #!/usr/bin/env python3
# """ MongoDB Operations with Python using pymongo """
# from pymongo import MongoClient


# def Print_Nginx(nginx_collection):
#     Nlog = nginx_collection.count_documents({})
#     print("{} logs".format(Nlog))
#     get_method = len(list(nginx_collection.find({'method': "GET"})))
#     POST_method = len(list(nginx_collection.find({'method': "POST"})))
#     PUT_method = len(list(nginx_collection.find({'method': "PUT"})))
#     PATCH_method = len(list(nginx_collection.find({'method': "PATCH"})))
#     DELETE_method = len(list(nginx_collection.find({'method': "DELETE"})))
#     print("Methods:\n\tmethod GET:{}\n\tmethod POST: {}\n\tmethod PUT: "
#           "{}\n\tmethod PATCH: {}\n\tmethod DELETE: {}"
#           .format(get_method, POST_method, PUT_method,
#                   PATCH_method, DELETE_method))
#     status_check = len(list(nginx_collection.find({
#         'method': "GET", 'path': '/status'})))
#     print("{} status check".format(status_check))


# def run():
#     '''Provides some stats about Nginx logs stored in MongoDB.'''
#     client = MongoClient('mongodb://127.0.0.1:27017')
#     Print_Nginx(client.logs.nginx)


# if __name__ == '__main__':
#     run()
