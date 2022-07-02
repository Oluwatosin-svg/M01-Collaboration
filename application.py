from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120))
    publisher = db.Column(db.String(150))

    def __repr__(self):
        return f"{self.name} - {self.author} - {self.publisher}"


@app.route('/book')
def get_book():
    book = Book.query.all()

    output = []
    for book in book:
        book_data = {'name': book.name, 'author': book.author, 'publisher': book.publisher}
        output.append(book_data)
    return {"book": output}

