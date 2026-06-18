from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "YOUR_API_KEY"

@app.route('/', methods=['GET','POST'])
def weather():
    weather = None

    if request.method == 'POST':
        city = request.form['city']

        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

        data = requests.get(url).json()

        weather = data['main']['temp']

    return render_template('index.html', weather=weather)

app.run(debug=True)