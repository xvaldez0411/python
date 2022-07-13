from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
date = datetime.datetime.today()

class User:
    db = "login_and_registration"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.birthday = data['birthday']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def register_user(cls, data):
        query = "INSERT INTO users(first_name,last_name,email, birthday, password) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(birthday)s,  %(password)s);"
        return connectToMySQL(cls.db). query_db(query, data)

    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db). query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        user = cls(row)
        return user

    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db). query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        user = cls(row)
        return user

    @staticmethod
    def validate_register(user):
        is_valid = True
        user_in_db = User.get_user_by_email(user)
        bday = datetime.datetime.strptime(user['birthday'], '%Y-%m-%d')
        age = User.calculate_age(bday)
        if user_in_db:
            flash('Email is associated with another account')
            is_valid = False
        if len(user['first_name']) < 2:
            flash('First name must be at least 3 characters', "error")
            is_valid = False
        if len(user['last_name']) < 2:
            flash('Last name must be at least 3 characters', "error")
            is_valid = False
            # from datetime import date def calculate_age(born): today = date.today() return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        if age < 18:
            flash('You must be 18 or older to register', "error")
            is_valid = False
        if len(user['password']) < 8:
            flash('Password must be at least 8 characters', "error")
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash('Passwords must match')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid email address!')
            is_valid = False

        return is_valid

    @staticmethod
    def calculate_age(bday):
        age = date.year - bday.year - ((date.month, date.day) < (bday.month, bday.day))
        return age

    @staticmethod
    def validate_login(user):
        is_valid = True
        user_in_db = User.get_user_by_email(user)
        if not user_in_db:
            flash('Email is not associated with an account!')
            is_valid = False

        if not EMAIL_REGEX.match(user['email']):
                flash('Invalid email address!')
                is_valid = False

        if len(user['password']) < 8:
                flash('Password must be at least 8 characters', "error")
                is_valid = False
        return is_valid