from flask import Flask, render_template

app = Flask(__name__)

book_list = []

@app.route('/books', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/books/new', methods=['GET'])
def new_book():
  return render_template('new.html')

@app.route('/books/<int:id>', methods=['GET'])
def show_book():
  return render_template('show.html')

@app.route('/books/<int:id>/edit', methods=['GET'])
def edit_book():
  return render_template('edit.html')

if __name__ == '__main__':
  app.run(debug=True, port=3000)

