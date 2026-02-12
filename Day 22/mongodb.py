from pymongo import MongoClient

# Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create / Access Database
db = client["company_db"]

# Create / Access Collection
collection = db["employees"]

print("Connected successfully!")
