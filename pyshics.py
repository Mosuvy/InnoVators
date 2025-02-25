from flask import Flask,jsonify,request

app = Flask(__name__)

# @app.route('/')
# def entry_point():
#     return 'Hello World'

@app.route('/', methods = {'GET'})
def entry_point():
    return jsonify(message="Hello World")

@app.route('/test', methods = {'POST', 'GET'})
def salam_sehat():
    if(request.method == "POST"):
        return jsonify(message="Salam POST untuk kita semua")
    elif(request.method == "GET"):
        return jsonify(message="Salam GET untuk kita semua")
    
    
if __name__ == '__main__':
    app.run(debug=True)