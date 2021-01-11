from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/hello-pardeep')
def index():
	return 'Hello, Pardeep!'

@app.route('/Avee')
def mydata():
    age = 2*4
    retJson = {
        'Name':'Avee Chahal',
        'Age': age

    }
    return jsonify(retJson)

@app.route('/add_two_nums', methods=["POST"])
def add_two_nums():
    # Get x and y
    dataDict = request.get_json(force=True)
#    if "y" not in dataDict:
#        return "ERROR", 305
    x = dataDict["x"]
    y = dataDict["y"]

    #Add z=x+y
    z = x+y
    # Prepare Json response
    retJSON = {
        "z": z
    }
    return jsonify(retJSON), 200

if __name__ == '__main__':
	app.run(debug=True)