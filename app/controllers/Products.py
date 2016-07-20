"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        """
        This is an example of loading a model.
        Every controller has access to the load_model method.
        """
        self.load_model('Product')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        all_products = self.models['Product'].get_all_products()
        return self.load_view('index.html', products = all_products)

    def new(self):
        return self.load_view('add_product.html')

    def edit(self, id):
        product = self.models['Product'].view_product(id)
        return self.load_view('edit_product.html', product= product[0])

    def show(self, id):
        product = self.models['Product'].view_product(id)
        return self.load_view('view_product.html', product=product[0])

    def create(self):
        self.models['Product'].add_product(request.form)
        return redirect('/')

    def destroy(self, id):
        self.models['Product'].delete_product(id)
        return redirect ('/')

    def update(self):
        self.models['Product'].modify_product(request.form)
        return redirect ('/')

    def goback(self):
        return redirect ('/')
