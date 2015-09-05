from flask import render_template
from app import app
import os

@app.route("/")
def index():
    return '<h1>pyPageScreenshot</h1>'

@app.route("/convert/<productCode>/<queryString>")
def convert(productCode, queryString):
    os.system('python screenshot.py %s "http://127.0.0.1:3000/mandala/%s" &' % (productCode, queryString))
    return "<h1>Finalizado</h1>Imagem da mandala => <a href='/image/"+productCode+"'>"+productCode+"</a>" 

@app.route("/mandala/<queryString>")
def mandala(queryString):
    return render_template('mandala.html', queryString = queryString)

@app.route("/image/<productCode>")
def image(productCode):
    return render_template('image.html', imagePath = productCode +".png")

        