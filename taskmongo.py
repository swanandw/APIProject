from flask import Flask,request,jsonify
import pymongo
import ssl
ssl_cert_reqs=ssl.CERT_NONE

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://prashant:palkar@cluster0.hee8g.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

database = client['taskdb']
collection = database['taskcollection']

@app.route("/insert/mongo",methods =['POST'])
def insert():
    if request.method == 'POST':
        name= request.json['name']
        number = request.json['number']
        collection.insert_one({name:number})
        return  jsonify(str("successfully inserted"))

@app.route("/update/mongo",methods =['POST'])
def update():
    if request.method == 'POST':
        name= request.json['name']
        number = request.json['number']
        collection.update_one({name,number})
        return  jsonify(str("successfully updated"))

if __name__ == '__main__':
    app.run(port=5001)