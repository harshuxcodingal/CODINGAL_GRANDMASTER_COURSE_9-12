from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def bmi():

    result = None

    if request.method == 'POST':

        weight = float(request.form['weight'])
        height = float(request.form['height'])

        result = weight / (height ** 2)

    return render_template('index.html', bmi=result)

app.run(debug=True)