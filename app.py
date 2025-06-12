import json

from flask import  Flask
import sqlalchemy
import sqlite3
from data_models import *


app = Flask(__name__)

@app.route("/",methods=["GET"])
def get():
    return {"status":"success","message":"Flask app is working fine."}

@app.route("/phones",methods=["GET"])
def get_phones():
    data = get_all()
    data_parsed = [{"id":dat.id,"Title":dat.title,"Price":dat.price,"Currency":dat.currency,"Ram":dat.ram,"Storage":dat.storage} for dat in data]
    return {"status":"success","Products": data_parsed }

@app.route("/phones/<phone_id>",methods=["GET"])
def phone_by_id(phone_id):
    data = get_data_by_id(phone_id)
    record = {"id":data.id,"Title":data.title,"Price":data.price,"Currency":data.currency,"Ram":data.ram,"Storage":data.storage}
    return {"status" : "success", "Data" : record}


if __name__ == "__main__":
    app.run(port=8000,debug=True)
