#!/usr/bin/env python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for, flash
from forms import MusicSearchForm, AlbumForm
from models import Album, Artist
from app import app, db
from db_setup import init_db, db_session
from tables import Results



init_db()

#app = Flask(__name__)
# app.config['SECRET_KEY'] = 'ranjani'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ranjani:SRbravard@94@localhost:5432/postgres'
# db = SQLAlchemy(app)

#from models import User
# class User(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	username = db.Column(db.String(50), unique=True)
# 	email = db.Column(db.String(120), unique=True)

# 	def __init__(self, username, email):
# 		self.username = username
# 		self.email = email

@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/charts')
def charts():
	return render_template('charts.html')

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/tables')
def tables():
	return render_template('tables.html')

@app.route('/blank')
def blank():
	return render_template('blank.html')

@app.route('/login')
def login():
	return render_template('login.html')

##################################################################
	

# @app.route('/', methods=['GET','POST'])
# def add_user():
# 	#form = invoiceForm(request.form)
# 	myUser = User.query.all()
# 	return render_template('add_user.html', myUser = myUser)

# @app.route('/test_view_invoice', methods=['GET','POST'])
# def test_view_invoice():
	
# 	return render_template('test_view_invoice.html')



# @app.route('/post_user', methods=['POST'])
# def post_user():
# 	user = User(request.form['username'], request.form['email'])
# 	db.session.add(user)
# 	db.session.commit()
# 	return redirect(url_for('add_user'))

# if __name__ == '__main__':
# 	app.run(debug=True)



	
######################################################################


@app.route('/', methods=['GET', 'POST'])
def index1():
    search = MusicSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
 
    return render_template('index1.html', form=search)
 
 
@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']
 
    if search.data['search'] == '':
        qry = db_session.query(Album)
        results = qry.all()
 
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Results(results)
        table.border = True
        return render_template('results.html', table=table)
 
 
@app.route('/new_album', methods=['GET', 'POST'])
def new_album():
    """
    Add a new album
    """
    form = AlbumForm(request.form)
    if request.method == 'POST' and form.validate():
        # save the album
        album = Album()
        save_changes(album, form, new=True)
        flash('Album created successfully!')
        return redirect('/')
    return render_template('new_album.html', form=form)


def save_changes(album, form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    artist = Artist()
    artist.name = form.artist.data
 
    album.artist = artist
    album.title = form.title.data
    album.release_date = form.release_date.data
    album.publisher = form.publisher.data
    album.media_type = form.media_type.data
 
    if new:
        # Add the new album to the database
        db_session.add(album)
 
    # commit the data to the database
    db_session.commit()

@app.route('/item/<int:id>', methods=['GET', 'POST'])
def edit(id):
    qry = db_session.query(Album).filter(
                Album.id==id)
    album = qry.first()

    if album:
        form = AlbumForm(formdata=request.form, obj=album)
        if request.method == 'POST' and form.validate():
            # save edits
            save_changes(album, form)
            flash('Album updated successfully!')
            return redirect('/')
        return render_template('edit_album.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)
 
 
if __name__ == '__main__':
    app.run(debug=True)