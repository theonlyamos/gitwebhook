#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2020-01-03 06:53:50
# @Author  : Amos Amissah (theonlyamos@gmail.com)
# @Link    : https://github.com/theonlyamos/gitwebhook.git
# @Version : 1.0.0

from flask import Flask, jsonify, request
from subprocess import check_output
from os import path, chdir, popen
import json

app = Flask(__name__)
app.secret_key = "8sa0fdsuo43fdjiofs90dfasdfa0"

@app.route("/gitwebhook", methods=["GET", "POST"])
def index():
    domain = request.args.get('domain')
    data = request.get_json()
    response = json.loads(json.dumps(data))
    if request.method.lower() == "post":
        if response['ref'].split('/')[-1] == 'master':
            chdir("/var/www/html/"+domain)
            result = check_output(["git", "pull"])
            result = result.decode("utf-8")
            if domain.startswith('hermescraft'):
                popen('pm2 restart 0')
                popen('pm2 restart 1')
            chdir(path.dirname(path.abspath(__file__)))
            with open ("pulls.txt", "w") as file:
                json.dump(data, file)
            return jsonify({"status": "Success", "method": request.method})
        return jsonify({"status": "Failure", "message": "not master branch"})
    return jsonify({"status": "Failure", "message": "not a post request"})

if __name__ == "__main__":
    app.run(debug=False)
