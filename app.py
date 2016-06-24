from flask import Flask, render_template, request, redirect, url_for
from flask_modus import Modus
from book import Book

app = Flask(__name__)
modus = Modus(app)

book_list = []

@app.route('/books', methods=['GET'])
def index():
  return render_template('index.html', book_list=book_list)

@app.route('/books/new', methods=['GET'])
def new_book():
  return render_template('new.html')

@app.route('/books', methods=['POST'])
def create_book():
  new_book = Book(request.form['title'], request.form['author'])
  book_list.append(new_book)
  return redirect(url_for('index'))


@app.route('/books/<int:id>', methods=['GET'])
def show_book():
  return render_template('show.html')

@app.route('/books/<int:id>', methods=["DELETE"])
def delete_book():
  return redirect(url_for('index'))


@app.route('/books/<int:id>/edit', methods=['GET'])
def edit_book():
  return render_template('edit.html')

if __name__ == '__main__':
  app.run(debug=True, port=3000)

