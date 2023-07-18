from flask import request
from pymongo import MongoClient

from ui.src.constants import MONGO_URI, DB_NAME, DATA_ENDPOINT_COLLECTION


def insert_data_endpoint():
    # Extract form data
    type = request.form['type']
    owner = request.form['owner']
    username = request.form['username']
    password = request.form['password']
    host = request.form['host']
    port = int(request.form['port'])
    database = request.form['database']

    # Connect to MongoDB Atlas
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[DATA_ENDPOINT_COLLECTION]

    # Create a new document
    data = {
        'type': type,
        'owner': owner,
        'username': username,
        'password': password,
        'host': host,
        'port': port,
        'database': database
    }

    # Insert the document into the collection
    result = collection.insert_one(data)