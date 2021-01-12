import pymongo


class Database(object):
    # Default URI!
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None
    Collection = "todoapp"

    # Initializing our client.
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['todo']

    # Adding some useful methods: insert, remove, find, find_one.
    @staticmethod
    def insert(data):
        Database.DATABASE[Database.Collection].insert(data)

    @staticmethod
    def remove(query):
        Database.DATABASE[Database.Collection].remove(query)

    @staticmethod
    def find(query):
        return Database.DATABASE[Database.Collection].find(query)

    @staticmethod
    def find_one(query):
        return Database.DATABASE[Database.Collection].find_one(query)
    
    @staticmethod
    def replace_one(before, after):
        Database.DATABASE[Database.Collection].replace_one(before, after)
