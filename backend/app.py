from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

MONGO_URI = os.environ.get("MONGO_URI")

if not MONGO_URI:
    raise Exception("MONGO_URI is not set! Check your environment variables.")

client = MongoClient(MONGO_URI)
db = client.dockeruser
collection = db.users

print("✅ Connected to MongoDB successfully")

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
    print("🚀 Backend running on port 5000")
    app.run(host="0.0.0.0", port=5000)
