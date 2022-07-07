from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User

@app.route('/')
def dashboard():
    return redirect('/users')

@app.route('/users')
def show_all():
    return render_template('all_users.html', users=User.get_all())

@app.route('/users/new')
def create():
    User.save(request.form)
    return render_template('create_new.html')

@app.route('/users/new', methods=['POST'])
def add_new():
    User.save(request.form)
    return redirect('/users')

@app.route('/users/<int:id>')
def show_user(id):
    data = {
        "id": id
    }
    return render_template('show_user.html', user=User.get_user(data))

@app.route('/users/<int:id>/edit')
def show_edit_form(id):
    data = {
        "id": id
    }
    return render_template("edit_user.html", user=User.get_user(data))

@app.route('/users/<int:id>/update', methods=['POST'])
def update_user(id):
    User.update(request.form)
    return redirect('/users')

@app.route('/users/<int:id>/delete')
def delete_user(id):
    data = {
    "id": id
    }
    User.delete(data)
    return redirect('/users')