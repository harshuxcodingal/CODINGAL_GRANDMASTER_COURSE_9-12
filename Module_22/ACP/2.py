from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def difference():

    days = None

    if request.method == 'POST':

        date1 = datetime.strptime(request.form['date1'], "%Y-%m-%d")
        date2 = datetime.strptime(request.form['date2'], "%Y-%m-%d")

        days = abs((date2 - date1).days)

    return render_template('index.html', days=days)

app.run(debug=True)