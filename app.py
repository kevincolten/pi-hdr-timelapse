from flask import Flask, render_template, jsonify, request
from json import dumps
from subprocess import call
from os import path, makedirs
from shutil import rmtree
application = Flask(__name__)

@application.route("/")
def index():
    return render_template('index.html')

@application.route("/run", methods=["GET", "POST"])
def run():
    if request.method == "GET":
        if path.exists('static/picams/'):
            return jsonify({'complete': true})
        return jsonify({"complete": False})
    if request.method == "POST":
        form = request.form.to_dict();
        for num in xrange(int(form['nimages'])):
            call(['sshpass -v -p hello123 ssh -oStrictHostKeyChecking=no pi@picam' + str(num + 1) + ".local 'python ~/pi-hdr-timelapse/runhdrpi.py '" + dumps(form) + "' &> log.txt'"], shell=True)
        return jsonify({"request": form })

if __name__ == "__main__":
    application.run(host='0.0.0.0')
