# from flask_wtf import Form
# from wtforms import StringField, TextAreaField,SelectField,DateField
# from wtforms.validators import InputRequired, Length
# from wtforms_components import DateRange
# from datetime import date

# class invoiceForm(Form):
# 	username = StringField('username')
# 	email = StringField('email')
# 	submit = submitField('submit')


# forms.py

from wtforms import Form, StringField, SelectField, validators

class MusicSearchForm(Form):
    choices = [('Invoice Number', 'Invoice Number'),
               ('Status', 'Status')]
    select = SelectField('Search for Invoice:', choices=choices)
    search = StringField('')


class AlbumForm(Form):
    media_types = [('Sent', 'Sent'),
                   ('Paid', 'Paid'),
                   ('Cancel', 'Cancel'),
                   ('Pending', 'Pending')]
    
    artist = StringField('Invoice Title')
    title = StringField('Invoice Number')
    release_date = StringField('Name')
    publisher = StringField('Email')
    media_type = SelectField('Status', choices=media_types)
    #due_date = StringField('Due_date')
