from flask import render_template
from app import app
import os
from convert import Convert

@app.route("/")
def index():
    return 'index'

@app.route("/convert/<productCode>/<queryString>")
def convert(productCode, queryString):
    os.system('python screenshot.py %s "http://127.0.0.1:4000/mandala/%s" &' % (productCode, queryString))
    #os.spawnl(os.P_NOWAIT, "python screenshot.py %s 'http://127.0.0.1:9000/mandala/%s'" % (productCode, queryString))
    return 'ok'

@app.route("/mandala/<queryString>")
def mandala(queryString):
    return render_template('mandala.html', queryString = queryString)

        