from mysqlconnection import connectToMySQL
from flask import flash

class User:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
        
    # @staticmethod
    # def validate(form_data):
    #     if len(form_data.get('first_name')) <=0:
    #         flash ('First Name Needed')
    #     else:
    #         return 
    
    @classmethod
    def get_all(cls):
        query= "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users=[]
        for u in results:
            users.append(cls(u))
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);" 
        result = connectToMySQL('users_schema').query_db(query,data)
        return result

    @classmethod
    def get_one(cls,data):
        query='SELECT * FROM users WHERE id =%(id)s';
        result = connectToMySQL('users_schema').query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def update(cls,data):
        query='UPDATE users SET first_name=%(first_name)s,last_name=%(first_name)s,email_name=%(first_name)s,updated_at=NOW() WHERE id=%(id)s;'  
        return connectToMySQL ('users_schema').query_db(query,data)

    @classmethod
    def remove(cls,data):
        query='DELETE FROM users WHERE id= %(id)s;'
        return connectToMySQL('users_schema').query_db(query,data)