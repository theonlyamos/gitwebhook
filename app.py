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
    if request.method.lower() == "post":
        chdir("/var/www/html/"+domain)
        result = check_output(["git", "pull"])
        result = result.decode("utf-8")
        print(result)
        if domain.startswith('hermescraft'):
            popen('pm2 restart 0')
            popen('pm2 restart 1')
        data = request.get_json()
        print(json.dumps(data))
        chdir(path.dirname(path.abspath(__file__)))
        with open ("pulls.txt", "w") as file:
            json.dump(data, file)
    return jsonify({"success": True, "method": request.method})

if __name__ == "__main__":
    app.run(debug=True)
