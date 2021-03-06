# from config import app
from flask import Flask, request, Response
from api.resources import CategoryResource, ProductResource, SubCategoryResource
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

api.add_resource(CategoryResource, '/api/category/', '/api/category/<string:cat_id>')
api.add_resource(SubCategoryResource, '/api/subcategory/<string:cat_id>')

api.add_resource(ProductResource, '/api/product/', '/api/product/<string:prod_id>')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6000, debug=True)