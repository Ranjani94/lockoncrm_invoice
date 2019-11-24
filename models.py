
# from app import db


#     # def serialize(self):
#     #     return {
#     #         'id': self.id, 
#     #         'name': self.name,
#     #         'author': self.author,
#     #         'published':self.published
#     #     }


# class User(db.Model):
#     __tablename__ = 'invoice_form'

#     id = db.Column(db.Integer, primary_key=True)
#     invoice_title= db.Column(db.String(20), unique=True, nullable=False)
#     status = db.Column(db.Enum('paid','sent','pending','cancel'),default='untouched')
#     invoice_number = db.Column(db.String(10), unique=True, nullable=False)
#     name = db.Column(db.String(50), unique=True)
#     email = db.Column(db.String(50), unique=True, nullable=False)
#     phone = db.Column(db.Integer, unique=True)
#     due_date = db.Column(db.DateTime)
#     address_line = db.Column(db.String(50), unique=True)
#     street = db.Column(db.String(50), unique=True)
#     city = db.Column(db.String(30), unique=True)
#     state = db.Column(db.String(20), unique=True)
#     postcode = db.Column(db.Integer, unique=True)
#     country = db.Column(db.Enum('GB','AF','AX','AL','DZ'))
#     total_amount = db.Column(db.Numeric)
    
#     def __init__(self, invoice_title, status, invoice_number, name, email, phone, due_date, address_line, street, city, state, postcode, country,total_amount):
#         self.invoice_title = invoice_title
#         self.status = status
#         self.invoice_number = invoice_number
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.due_date = due_date
#         self.address_line = address_line
#         self.street = street
#         self.city = city
#         self.state = state
#         self.postcode = postcode
#         self.country = country
#         self.total_amount = total_amount
        
#     def __repr__(self):
#         return '<id {}>'.format(self.id)

########################################################


from app import db


class Artist(db.Model):
    __tablename__ = "artists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return "{}".format(self.name)

    # def __init__(self, name):
    #     """"""
    #     self.name = name  


class Album(db.Model):
    """"""
    __tablename__ = "albums"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.String)
    publisher = db.Column(db.String)
    media_type = db.Column(db.String)

    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"))
    artist = db.relationship("Artist", backref=db.backref(
        "albums", order_by=id), lazy=True)
