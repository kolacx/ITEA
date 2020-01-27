from marshmallow import fields, Schema, validates

class ProjectSchema(Schema):

    title = fields.String()
    description = fields.String()
    deadline = fields.DateTime()


class DevelopersSchema(Schema):

    id = fields.String()
    fullname = fields.String(required=True)
    position = fields.String(required=True)
    project = fields.Nested(ProjectSchema, dump_only=True)
