# myapp/mongo_utils.py

from pymongo import MongoClient
from django.conf import settings

# MongoDB connection setup
client = MongoClient(settings.MONGO_CONNECTION_STRING)
db = client[settings.MONGO_DATABASE_NAME]  # Replace with your database name
