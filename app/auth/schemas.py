from marshmallow import Schema, fields

class UserSchema(Schema):
    username = fields.Str()
    email = fields.Email()
    password = fields.Str()
    deleted = fields.Bool()

    