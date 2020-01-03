#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2020-01-03 06:53:50
# @Author  : Amos Amissah (theonlyamos@gmail.com)
# @Link    : https://github.com/theonlyamos/gitwebhook.git
# @Version : 1.0.0

from flask import Flask, jsonify, request
from subprocess import check_output
from os import path, chdir

app = Flask(__name__)
app.secret_key = "8sa0fdsuo43fdjiofs90dfasdfa0"

@app.route("/gitwebhook", methods=["GET", "POST"])
def index():
    if request.method.lower() == "post":
        chdir("/var/www/html/openmart.ga")
        result = check_output(["git", "pull"])
        result = result.decode("utf-8")
        print(result)
        data = request.get_json();
        print(data)
        chdir(path.abspath(__file__))
        with open ("pulls.txt", "a+") as file:
            file.write("\n\n" + str(data))
    return jsonify({"success": True, "method": request.method})

if __name__ == "__main__":
    app.run(debug=True)