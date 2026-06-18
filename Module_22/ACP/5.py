from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def resume():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']

        return render_template(
            'resume.html',
            name=name,
            email=email,
            mobile=mobile
        )

    return render_template('form.html')

app.run(debug=True)