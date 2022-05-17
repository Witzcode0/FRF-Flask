from marshmallow import Schema, fields

class PostSchema(Schema):
    title = fields.Str()
    content = fields.Str()
    deleted = fields.Bool()
