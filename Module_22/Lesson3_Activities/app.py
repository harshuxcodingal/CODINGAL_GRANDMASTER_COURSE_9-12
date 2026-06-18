from flask import Flask, render_template
import folium

app = Flask(__name__)

@app.route('/')
def map():

    m = folium.Map(location=[19.9975,73.7898], zoom_start=12)

    folium.Marker(
        [19.9975,73.7898],
        tooltip="Nashik"
    ).add_to(m)

    m.save("templates/map.html")

    return render_template("map.html")

app.run(debug=True)