from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/dashboard")
def user_dashboard():
    user_data = {
        'id': session['user_id']
    }
    user = User.get_user_by_id(user_data)
    recipes = Recipe.get_all()
    return render_template('dashboard.html', user=user, recipes=recipes)

@app.route('/recipes/new')
def new_recipe_form():
    user_data = {
        'id': session['user_id']
    }
    user = User.get_user_by_id(user_data)
    return render_template('create_recipe.html', user=user)

@app.route('/recipes/create', methods=['POST'])
def create_recipe():
    if not Recipe.validate_create(request.form):
        return redirect('/recipes/new')
    Recipe.create(request.form)
    return redirect('/dashboard')

@app.route('/recipes/<int:id>')
def show_recipe(id):
    user_data = {
        'id': session['user_id']
    }
    user = User.get_user_by_id(user_data)
    recipe_data = {
        'id': id
    }
    recipe = Recipe.get_one(recipe_data)
    return render_template('show_recipe.html', recipe=recipe, user=user)

@app.route('/recipes/<int:id>/edit')
def show_edit_form(id):
    user_data = {
        'id': session['user_id']
    }
    user = User.get_user_by_id(user_data)
    recipe_data = {
        'id': id
    }
    recipe = Recipe.get_one(recipe_data)
    if(recipe.user_id != user.id):
        flash('Unauthorized access to edit recipe with id {id}')
        return redirect('/dashboard')

    return render_template('edit_recipe.html', user=user, recipe=recipe)

@app.route('/recipes/<int:id>/update', methods=['POST'])
def update_recipe(id):
    Recipe.update(request.form)
    return redirect('/dashboard')

@app.route('/recipes/<int:id>/delete')
def delete(id):
    recipe_data = {
        'id': id
    }
    recipe = Recipe.get_one(recipe_data)
    if(recipe.user_id != session['user_id']):
        flash('Unauthorized access to edit recipe with id {id}')
        return redirect('/dashboard')
    Recipe.delete(recipe_data)
    return redirect('/dashboard')