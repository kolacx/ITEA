from marshmallow import fields, Schema, validates

class UserSchema(Schema):

    telegram_id = fields.String()
    username = fields.String()
    phone_number = fields.String()
    email = fields.Email()


class CategorySchema(Schema):

    id = fields.String()
    title = fields.String(required=True)
    description = fields.String(required=True)
    subcategories = fields.List(fields.Nested('CategorySchema'))
    is_root = fields.Boolean(required=True)


class ProductSchema(Schema):

	id = fields.String()
	title = fields.String(required=True)
	description = fields.String(required=True)
	article = fields.String(required=True)
	price = fields.Integer(required=True)
	in_stock = fields.Integer(required=True)
	discount_price = fields.Integer()
	extra_data = fields.String()
	category = fields.Nested(CategorySchema, required=True)