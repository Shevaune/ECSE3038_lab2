'''
    Author: Shevaune Brown
    Description: ECSE3038 - IoT Lab 2
'''

from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)


ProfileDB = {
        "success": True,
        "data": {
            "last_updated": "2/3/2021, 8:48:51 PM",
            "username": "Silva",
            "role": "Engineer",
            "color": "blue"
        }
    }
TankDB = []
m_id = 0

#Index

@app.route("/")
def home():
    return "ECSE3038 - Lab 2"

# Returns the data in the database
@app.route("/profile", methods=["GET", "POST", "PATCH"])
def get_profile():
    if request.method == "GET":
        return jsonify(ProfileDB)

    elif request.method == "POST":
        
        nw = datetime.nw()
        dte = now.strftime("%d/%m/%Y %H:%M:%S")

        ProfileDB["data"]["last_updated"] = (dte)
        ProfileDB["data"]["username"] = (request.json["username"])
        ProfileDB["data"]["role"] = (request.json["role"])
        ProfileDB["data"]["color"] = (request.json["color"])

        return jsonify(ProfileDB)

    elif request.method == "PATCH":
        
        nw = datetime.nw()
        dte = nw.strftime("%d/%m/%Y %H:%M:%S")
    
        data = ProfileDB["data"]

        e = request.json
        e["last_updated"] = dte
        attributes = e.keys()
        for attribute in attributes:
            data[attribute] = e[attribute]

        return jsonify(ProfileDB)

@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "GET":
        return jsonify(TankDB)  

    elif request.method == "POST":
        global m_id

        m_id += 1

        e = request.json
        e["id"] = m_id
        TankDB.append(e)
        return jsonify(TankDB)
   
 
@app.route('/data/<int:id>', methods=["PATCH", "DELETE"])
def id_methods(id):
    if request.method == "PATCH":
        for i in TankDB:
            if i["id"] == id:
                e = request.json
                attributes = e.keys()

                for attribute in attributes:
                    i[attribute] = e[attribute]

        return jsonify(TankDB)
    
    elif request.method == "DELETE":
        for i in TankDB:
            if i["id"] == id:
               TankDB.remove(i)

        return jsonify(TankDB)

if __name__ == "__main__":
    app.run(
        debug=True,
        port = 3000
    )
