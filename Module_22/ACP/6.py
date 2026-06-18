from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def resume():

    if request.method == 'POST':

        data = {
            "name": request.form['name'],
            "email": request.form['email'],
            "mobile": request.form['mobile'],
            "skills": request.form['skills'],
            "education": request.form['education']
        }

        return render_template('resume.html', data=data)

    return render_template('form.html')

app.run(debug=True)