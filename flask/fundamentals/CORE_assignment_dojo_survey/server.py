from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "ssssshhhhhhh"

@app.route('/')
def form_page():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def function():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')




if __name__=="__main__":
    app.run(debug=True)