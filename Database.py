from pymongo import MongoClient
import os
class Database:
    HOST = os.environ['DB_HOST']
    DB_PORT = '27017'
    DB_NAME = 'test'

    def __init__(self):
        self._db_conn =MongoClient(f'mogodb://{Database.HOST}:{Database.PORT}')
        self._db = self._db_conn[Database.DB_NAME]

    def get_single_data(self, collection, key):
        db_collection = self._db[collection]
        document = db_collection.find_one(key)
        return document

    def get_multiple_data(self, collection, key):
        db_collection = self._db[collection]
        documents = db_collection.find(key)
        return documents

    def insert_single_data(self, collection, data):
        db_collection = self._db[collection]
        document = db_collection.insert_one(data)
        return document.inserted_id

    def insert_multiple_data(self, collection, data):
        db_collection = self._db[collection]
        result = db_collection.insert_many(data)
        return result.inserted_ids

    def aggregate(self, collection, pipeline):
        db_collection = self._db[collection]
        documents = db_collection.aggregate(pipeline)
        return documents
    def update_single_data(self,collection, condition, new_doc):
        db_collection = self._db[collection]
        document = db_collection.find_one(condition)
        if(document is None):
            result = db_collection.insert_one(new_doc)
            return result
        elif condition is None:
            return None
        else:
            result = db_collection.update_one(condition,new_doc)
            return result
    def update_multiple_data(self,collection,condition, new_docs):
        db_collection = self._db[collection]
        documents = db_collection.find(condition)
        if(documents is None):
            result = db_collection.insert_many(new_docs)
            return result
        elif condition is None:
            return None
        else:
            result = db_collection.update_many(condition,new_docs)
            return result