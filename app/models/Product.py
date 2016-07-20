""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Product(Model):
    def __init__(self):
        super(Product, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """
    def get_all_products(self):
        return self.db.query_db("SELECT * FROM products")

    def view_product(self, product_id):
        query = "SELECT * from Products where Products.id = :id"
        data = {'id': product_id}
        return self.db.query_db(query,data)

    def add_product(self, product):
        query = 'INSERT INTO Products (Name, Description, Price, created_at, updated_at) VALUES (:product_name, :product_description, :product_price, NOW(), NOW())'
        data = {'product_name':product['product_name'],'product_description':product['product_description'], 'product_price':product['product_price']}
        return self.db.query_db(query,data)

    def delete_product(self, product_id):
        query = 'DELETE FROM Products WHERE Products.id = :id'
        data = {'id' :product_id}
        return self.db.query_db(query,data)

    def modify_product(self, product):
        query = 'UPDATE Products SET Name= :name, Description= :description, Price= :price, updated_at= NOW() WHERE Products.id= :id'
        data = {'id':product['id'], 'name':product['product_name'], 'description':product['product_description'], 'price':product['product_price']}
        return self.db.query_db(query,data)

        