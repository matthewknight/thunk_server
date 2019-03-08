from flask import Flask, request

app = Flask(__name__)


@app.route("/thunk", methods=['GET', 'POST'])
def processThunk():
    if request.method == "GET":
        return "SENDING THUNK"

    elif request.method == "POST":
        return "INSERTING NEW THUNK"
