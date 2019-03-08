from flask import Flask, request
from tinydb import TinyDB
import random

app = Flask(__name__)
thunkDB = TinyDB('thunks.json')

@app.route("/thunk", methods=['GET', 'POST'])
def processThunk():
    if request.method == "GET":
        return random.choice(thunkDB.all())['thunkContent']

    elif request.method == "POST":
        thunkDB.insert(request.get_json())
        return 'Inserted thunk'