from flask import Flask, request, render_template, abort
import pandas as pd
import pickle


# Declare a Flask app
app = Flask(__name__)

class EdgeDevice:
    def __init__(self, key, name, lat, lng):
        self.key = key
        self.name=name
        self.lat = lat
        self.lng = lng

devices = (EdgeDevice ('1','Albany','42','-73'), EdgeDevice ('2','Los Angeles','34','-118'))
devices_by_key = {device.key: device for device in devices}


@app.route('/', methods=['GET', 'POST'])
def main():
    # If a form is submitted
    if request.method == "POST":

        # Unpickle classifier
        with open('model.pkl', 'rb') as f:
            clf = pickle.load(f)

        # Get values through input bars
        temperature = request.form.get("temperature")
        humidity = request.form.get("humidity")
        pressure = request.form.get("pressure")
        precipitation = request.form.get("precipitation")
        cloudCover = request.form.get("cloudCover")
        elevation = request.form.get("elevation")

        # Put inputs to dataframe
        X = pd.DataFrame([[temperature, humidity, pressure, precipitation, cloudCover, elevation]],
                         columns=["temperature", "humidity", "pressure", "precipitation", "cloudCover", "elevation"])

        # Get prediction
        prediction = clf.predict_proba(X)[0][1]

    else:
        prediction = ""

    return render_template("website.html", output=prediction)

@app.route("/3")
def index():
    return render_template('index.html', devices=devices)

@app.route("/<device_code>")
def show_device (device_code):
    device = devices_by_key.get(device_code)
    if device:
        return render_template('map.html', device=device)
    else:
        abort(404)


# Running the app
if __name__ == '__main__':
    app.run(debug = True)




