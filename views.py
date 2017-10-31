# coding:utf-8

import os, json, sqlite3
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from my_api.invoke_api import invoke_api


app = Flask(__name__)


@app.route('/upload', methods=['POST', 'GET'])


def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # current file path
        upload_path = os.path.join(basepath, 'upload', secure_filename(f.filename))  # need create 'upload' folder first
        f.save(upload_path)
        return redirect(url_for('list_uploaded_files'))
    return render_template('upload.html')


@app.route('/index')
def index():
    title = 'fortinet interview'
    user = 'ericwang'
    ip = request.remote_addr

    return render_template('index.html', title=title, user=user, ip =ip)


@app.route('/')
def hello_world():
    return "hahaa"



@app.route('/test')
def test():
    a = invoke_api()

    print a.get_file_report()
    return a.get_file_report()




@app.route('/file_listed')
def list_uploaded_files():
    return "test"



@app.route('/report')
def report():
    a = invoke_api()
    file_report = json.dumps(a.get_file_report())


    return render_template('check_report.html',file_report = file_report)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=8000)
