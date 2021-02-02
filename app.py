from flask import Flask, jsonify, render_template
from api.data import data_connector

app = Flask(__name__, static_url_path='')


# serve a html file from the flask app
@app.route('/')
def index():
    return render_template('html/index.html')

@app.route('/machinelearning')
def machinelearning():
    return render_template('html/machine_learning.html')

@app.route('/visualizations')
def visualizations():
    return render_template('html/graph.html')

# serve data from the flask app
@app.route('/data')
def data1():
    return jsonify(data_connector.get_data())

