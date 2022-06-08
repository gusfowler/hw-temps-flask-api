import subprocess

from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/temps")
def hello_world():
    stdOut = str(subprocess.check_output(['sensors']).decode("UTF-8"))
    output = []

    for line in stdOut.split("\n"):
        if line != '':
            output.append(line)

    print(output)
    return str(output)