from flask import Flask
from flask_sqlalchemy import SQLAlchemy, session

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)


new_book = Books(id=1, title="Harry Potter", author="J.K.Rowling", rating="9.3")


with app.app_context():
    # db.create_all()
    # db.session.add(new_book)
    # db.session.commit()
    all_books = Books.query.all()
    print(all_books[0])
    db.session.commit()
