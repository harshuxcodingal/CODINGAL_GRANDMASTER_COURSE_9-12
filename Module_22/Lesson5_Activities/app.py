from flask import Flask, request, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/', methods=['GET','POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if username == "admin" and password == "123":

            session['user'] = username

            return redirect('/dashboard')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return "Welcome Admin"

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/')

app.run(debug=True)