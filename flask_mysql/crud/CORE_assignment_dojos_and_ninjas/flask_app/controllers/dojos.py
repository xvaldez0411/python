from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def dojo_dashboard():
    return render_template('dashboard.html')

@app.route('/dojos')
def show_all_dojos():
    return render_template('show_all_dojos.html', dojos=Dojo.get_all())

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojo(id):   
    dojo_data = {
        'id': id
    }
    return render_template("show_dojo.html", dojo=Dojo.get_one(dojo_data))