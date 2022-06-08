import subprocess

from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/sensors")
def sensors():
    json = str(subprocess.check_output(['sensors', '-j']).decode('UTF-8'))
    
    print(json)
    return json