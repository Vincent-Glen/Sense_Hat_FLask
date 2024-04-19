from flask import Flask, render_template, jsonify
from sensor_data import get_sensor_data, check_warnings

from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/data")
def getdata():
    temperature, humidity = get_sensor_data()
    warnings = check_warnings(temperature, humidity)
    return jsonify({
        'temperature': temperature,
        'humidity': humidity,
        'warnings': warnings
    })
