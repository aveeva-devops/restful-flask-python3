from flask import Flask, jsonify, request
from flask_restful import Api, Resource 

app_api = Flask (__name__)
api = Api(app_api)

def checkPostedData(postedData, functionName):
    if (functionName == "add" or functionName == "subtract" or functionName =="multiply"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200
    elif (functionName == "division"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        elif int(postedData["y"]) == 0:
            return 302
        else:
            return 200


class Add(Resource):
    def post(self):
        # If i am here, post method is executed
        # Step 1, get posted data
        postedData = request.get_json(force=True)

        # Verify data validation
        status_code = checkPostedData(postedData, "add")
        if status_code !=200 :
            retJson = {
                "Message": "An error has happened",
                "Status Code": status_code
            }
            return jsonify(retJson)
        # If I am here, status_code is 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x+y

        # Add posted data
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        # return posted data
        return jsonify(retMap)

class Subtract(Resource):
    def post(self):
        # If i am here, Subtract post method is executed
        # Step 1, get posted data
        postedData = request.get_json(force=True)

        # Verify data validation
        status_code = checkPostedData(postedData, "subtract")
        if status_code !=200 :
            retJson = {
                "Message": "An error has happened",
                "Status Code": status_code
            }
            return jsonify(retJson)
        # If I am here, status_code is 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        # Subtract the data
        ret = x-y

        # Add posted data
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        # return posted data
        return jsonify(retMap)

class Multiply(Resource):
    def post(self):
        # If i am here, Subtract post method is executed
        # Step 1, get posted data
        postedData = request.get_json(force=True)

        # Verify data validation
        status_code = checkPostedData(postedData, "multiply")
        if status_code !=200 :
            retJson = {
                "Message": "An error has happened",
                "Status Code": status_code
            }
            return jsonify(retJson)
        # If I am here, status_code is 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        # Multiply the data
        ret = x*y

        # Add posted data
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        # return posted data
        return jsonify(retMap)

class Divide(Resource):
    def post(self):
        # If i am here, Subtract post method is executed
        # Step 1, get posted data
        postedData = request.get_json(force=True)

        # Verify data validation
        status_code = checkPostedData(postedData, "division")
        if status_code !=200 :
            retJson = {
                "Message": "An error has happened",
                "Status Code": status_code
            }
            return jsonify(retJson)
        # If I am here, status_code is 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        # divide the data
        ret = (x*1.0)/y

        # Add posted data
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        # return posted data
        return jsonify(retMap)

api.add_resource(Add,"/add")
api.add_resource(Subtract,"/subtract")
api.add_resource(Multiply,"/multiply")
api.add_resource(Divide,"/division")

if __name__=="__main__":
    app_api.run(debug=True)