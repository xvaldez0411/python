from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

class Ninja:
    db = "dojos_and_ninjas_schema"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
        self.dojo = None

    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id;"
    #     results = connectToMySQL(cls.db).query_db(query)
    #     ninjas = []
    #     for row in results:
    #         # create review object
    #         ninja = cls(row)
    #         user_data = {
    #             'id': row['dojos.id'],
    #             'name': row['name'],
    #             'created_at': row['dojos.created_at'],
    #             'updated_at': row['dojos.updated_at'],
    #         }
    #         # create user object
    #         dojo=Dojo(user_data)
    #         # associate user to review
    #         ninja.dojo = dojo
    #         # add single review to list of all reviews
    #         ninjas.append(ninja)
    #     return ninjas

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id WHERE ninjas.id =%(id)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False

        row = results[0]
        ninja = cls(row)
        user_data = {
            'id': row['dojos.id'],
            'name': row['name'],
            'created_at': row['dojos.created_at'],
            'updated_at': row['dojos.updated_at'],
        }
        # create user object
        dojo_1=dojo.Dojo(user_data)
        ninja.dojo = dojo_1
        return ninja

    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas(first_name, last_name, age, dojo_id) VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        dojo_id = connectToMySQL(cls.db).query_db(query,data)