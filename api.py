from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime

app = Flask(__name__)

uri = "mongodb+srv://root:dika123@andhika.e99nw.mongodb.net/?retryWrites=true&w=majority&appName=Andhika"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client["sensor_data"]
collection = db["readings"]

# Endpoint untuk menerima data sensor
@app.route("/sensor-data", methods=["POST"])
def receive_sensor_data():
    data = request.json
    data["timestamp"] = datetime.now()
    collection.insert_one(data)
    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)