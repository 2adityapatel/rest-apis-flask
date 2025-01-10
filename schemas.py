from marshmallow import Schema,fields

class PlainItemSchema(Schema):
    # here we are using dump only in id , as it will only be used in returning
    # not in the json payload of request
    id = fields.Int(dump_only=True)
    # whereas name,price,store_id will be used in both json payload request and returning these fields
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    description = fields.Str(required=False)


class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()
    description = fields.Str()

class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema(), dump_only=True))


class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)

class TagSchema(PlainTagSchema):
    store_id = fields.Int(load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    items = fields.List(fields.Nested(PlainItemSchema(), dump_only=True))

class TagAndItemSchema(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema)
    tag = fields.Nested(TagSchema)

class UserSchema(Schema): 
    id = fields.Int(dump_omly=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)

# From documentation
# dump_only – If True skip this field during deserialization, 
# otherwise its value will be present in the deserialized object. 
# In the context of an HTTP API, this effectively marks the field as “read-only”.


# dump default
#  You use dump_default when you want a field to have a default value
# in the serialized output if it is missing from the data.


