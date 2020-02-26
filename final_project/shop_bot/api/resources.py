from flask_restful import Resource
from .schema import CategorySchema, ProductSchema
from models.model import Category, Product
from flask import request

class CategoryResource(Resource):

    def get(self, cat_id=None):

        query = Category.objects if not cat_id else Category.objects.get(id=cat_id)
        many = True if not cat_id else False

        return CategorySchema().dump(
            query,
            many=many
            )


    def post(self):
        err = CategorySchema().validate(
            request.json
            )

        if err:
            return err

        cat = Category(**request.get_json()).save()

        cat.reload()

        return CategorySchema().dump(cat)


    def delete(self, cat_id):

        try:
            cat = Category.objects.get(id=cat_id).delete()
            return 'deleted'
        except Exception as e:
            return str(e)


class ProductResource(Resource):

    def get(self, prod_id=None):

        query = Product.objects if not prod_id else Product.objects.get(id=prod_id)
        many = True if not prod_id else False

        return ProductSchema().dump(query, many=many)

    def post(self):

        cat = Category.objects.get(id=request.json['category'])

        req = request.get_json()
        req.pop('category')

        prod = Product(category=cat, **req).save()

        prod.reload()

        return ProductSchema().dump(prod)

    def delete(self, prod_id):

        try:
            prod = Product.objects.get(id=prod_id).delete()
            return '200'
        except Exception as e:
            return str(e)