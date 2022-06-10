import subprocess

from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/sensors")
def sensors():
    json = str(subprocess.check_output(['sensors', '-j']).decode('UTF-8'))

    return json

@app.route("/liquidctl")
def liquidctl():
    json = str(subprocess.check_output(['/usr/local/bin/liquidctl', '--json', 'status']).decode('UTF-8'))

    return json