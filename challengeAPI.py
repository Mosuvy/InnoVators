# challenge 1
# from flask import Flask,jsonify,request

# app = Flask(__name__)

# list_temp = []
# @app.route('/sensor1', methods = {'POST'})
# def simpan_data_sensor():
#     if(request.method == "POST"):
#         body = request.get_json()
#         temperature = body['temperature']
#         humidity = body['humidity']
#         timestamp = body['timestamp']
#         list_temp.append({
#             "temperature": temperature,
#             "humidity": humidity,
#             "timestamp": timestamp
#         })
#         print("Current Database:", list_temp, flush=True)
        
#         return{
#                 "message":"Hello, i have processed your request"   
#             }
    
    
# if __name__ == '__main__':
#     app.run(debug=True)

# challenge 2
from flask import Flask, jsonify, request

app = Flask(__name__)

# List kosong untuk menyimpan data
list_temp = []

# Endpoint untuk menyimpan data sensor dari Postman
@app.route('/sensor1', methods=['POST'])
def simpan_data_sensor():
    body = request.get_json()
    temperature = body['temperature']
    humidity = body['humidity']
    timestamp = body['timestamp']

    list_temp.append({
        "temperature": temperature,
        "humidity": humidity,
        "timestamp": timestamp
    })
    
    print("Current Database:", list_temp, flush=True)

    return jsonify({"message": "Data berhasil disimpan"})

# Endpoint untuk menghitung rata-rata temperature
@app.route('/sensor1/temperature/avg', methods=['GET'])
def hitung_rata_rata():
    if not list_temp:
        return jsonify({"error": "Tidak ada data temperature"}), 400

    total_temp = sum(d["temperature"] for d in list_temp)
    avg_temp = total_temp / len(list_temp)

    return jsonify({"average_temperature": avg_temp})

@app.route('/sensor1/humidity/avg', methods=['GET'])
def rata_rata():
    if not list_temp:
        return jsonify({"error": "Tidak ada data Humidity"}), 400

    total_temp = sum(d["humidity"] for d in list_temp)
    avg_temp = total_temp / len(list_temp)

    return jsonify({"average_humidity": avg_temp})

if __name__ == '__main__':
    app.run(debug=True)

