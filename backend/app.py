from flask import Flask, request, jsonify
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client.dockeruser
collection = db.users

@app.route("/add-user", methods=["POST"])
def add_user():
    data = request.json
    user = {
        "name": data["name"],
        "email": data["email"],
        "password": data["password"]
    }
    collection.insert_one(user)
    return jsonify({"message": "User added successfully"}), 201

@app.route("/users", methods=["GET"])
def get_users():
    users = []
    for user in collection.find():
        user["_id"] = str(user["_id"])
        users.append(user)
    return jsonify(users)

if __name__ == "__main__":
    print("Backend running successfully on port 5000")
    app.run(host="0.0.0.0", port=5000)


