from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")
    tags = db.relationship("TagModel", back_populates = "store", lazy="dynamic")

# when we call on any store, the StoreModel 
#  creates a query to fetch the store details
# for item details it needs to create another query to fetch all items
#  lazy dynamic is that , until we not mention or call it will not fetch item details

