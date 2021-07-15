from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key= "surevey key"

@app.route('/')
def survey():
    return render_template('index.html')

@app.route('/stuff', methods=['POST'])
def choose():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/submitted')

@app.route('/submitted')
def submissions():
    return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=True)