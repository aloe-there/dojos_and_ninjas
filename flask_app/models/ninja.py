from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.dojo_id = data["dojo_id"]

    @classmethod
    def get_all(cls):
        ninjas = []
        query = f"SELECT * FROM ninjas;"
        ninjas_from_db = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        for ninja in ninjas_from_db:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def get_all_from_dojo(cls, dojo_id):
        ninjas = []
        query = f"SELECT * FROM ninjas WHERE dojo_id={int(dojo_id)};"
        ninjas_from_db = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        for ninja in ninjas_from_db:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def add(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW());"
        new_ninja_id = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return new_ninja_id