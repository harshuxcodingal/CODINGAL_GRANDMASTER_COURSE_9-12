from flask import Flask, request, render_template

app = Flask(__name__)

users = []

@app.route('/', methods=['GET','POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        users.append({
            "username": username,
            "password": password
        })

        return "User Registered Successfully"

    return render_template('register.html')

app.run(debug=True)