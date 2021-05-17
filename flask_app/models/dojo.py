from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]

    @classmethod
    def get_all(cls):
        dojos = []
        query = "SELECT * FROM dojos;"
        dojos_from_db = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        for dojo in dojos_from_db:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def add(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        new_dojo_id = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return new_dojo_id

    @classmethod
    def get(cls, id):
        query = f"SELECT * FROM dojos WHERE id={id};"
        dojo = connectToMySQL('dojos_and_ninjas_schema').query_db(query)[0]
        return dojo