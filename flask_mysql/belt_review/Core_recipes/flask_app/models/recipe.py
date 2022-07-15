from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Recipe:
    db = "recipes_schema"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.cooking_time = data['cooking_time']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL(cls.db). query_db(query)
        recipes = []
        for row in results:
            recipe = cls(row)
            user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            user = User(user_data)
            recipe.user = user
            recipes.append(recipe)
        return recipes

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(cls.db). query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        recipe = cls(row)
        user_data = {
            'id': row['users.id'],
            'first_name': row['first_name'],
            'last_name': row['last_name'],
            'email': row['email'],
            'password': row['password'],
            'created_at': row['users.created_at'],
            'updated_at': row['users.updated_at']
        }
        user = User(user_data)
        recipe.user = user
        return recipe

    @classmethod
    def create(cls,data):
        query = "INSERT INTO recipes(name,description,instructions, date_made,cooking_time, user_id) VALUES(%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(cooking_time)s, %(user_id)s);"
        return connectToMySQL(cls.db). query_db(query, data)

    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, cooking_time = %(cooking_time)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db). query_db(query, data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s"
        return connectToMySQL(cls.db). query_db(query, data)

    @staticmethod
    def validate_create(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            flash('Name must be at least 3 characters', "error")
            is_valid = False
        if len(recipe['description']) < 3:
            flash('Description must be at least 3 characters', "error")
            is_valid = False
        if len(recipe['instructions']) < 3:
            flash('Instructions must be at least 3 characters', "error")
            is_valid = False
        if "cooking_time" not in recipe:
            flash('Must Select one')
            is_valid = False
        return is_valid