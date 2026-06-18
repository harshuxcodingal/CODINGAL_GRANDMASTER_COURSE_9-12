from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def leap():
    result = ""

    if request.method == 'POST':
        year = int(request.form['year'])

        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            result = "Leap Year"
        else:
            result = "Not Leap Year"

    return render_template('index.html', result=result)

app.run(debug=True)