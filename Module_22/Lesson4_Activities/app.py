from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def vowels():
    count = 0

    if request.method == 'POST':
        text = request.form['text']

        vowels = "aeiouAEIOU"

        for char in text:
            if char in vowels:
                count += 1

    return render_template('vowels.html', count=count)

app.run(debug=True)