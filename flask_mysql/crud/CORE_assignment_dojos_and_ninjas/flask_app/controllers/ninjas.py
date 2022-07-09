from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def create_ninja():
    return render_template('add_ninjas.html', dojos=Dojo.get_all())

@app.route('/ninjas/create', methods=['POST'])
def add_ninja():
    Ninja.save(request.form)
    return redirect('/ninjas')