from flask import Flask,jsonify
from pymongo import MongoClient
from uuid import uuid1
from flask import request

config = {
    "host": "localhost",
    "port": 27017,
    "username": "usmantahir",
    "password": "Ui8GdtammXFftMQU",
    "authSource": "admin"
}

class Connection:
    def __new__(cls, database):
        connection=MongoClient(**config)
        return connection[database]

app=Flask(__name__)
db=Connection('flask_mongo_crud')

@app.post("/user")
def insert_user():

    _id=str(uuid1().hex)
    
    content=dict(request.json)
    content.update({ "_id":_id })
    
    result =db.user.insert_one(content)
    if not result.inserted_id:
        return {"message":"Failed to insert"}, 500
    
    return {
        "message":"Success", 
        "data":{
            "id":result.inserted_id
            }
        }, 200

@app.get("/users")
def get_users():
    users=db.user.find({})
    return jsonify(list(users)),200

if __name__=="__main__":
    app.run(port=8887, debug=True)