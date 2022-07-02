from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "ssssshhhhhhh"

@app.route('/')
def main_page():
    if 'num' not in session:
        session['num'] = 0
    else:
        session['num'] += 1
    return render_template('index.html')

@app.route('/twice')
def twice():
    if 'num' not in session:
        session['num'] = 0
    else:
        session['num'] += 2
    return render_template('index.html')

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/user')

@app.route('/user',methods=['POST'])
def user():
    session['name'] = request.form["name"]
    return redirect('/')

@app.route('/user')
def user_get():
    return render_template('user.html')


if __name__=="__main__":
    app.run(debug=True)
