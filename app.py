from flask import Flask, render_template

app = Flask(__name__)

book_list = []

@app.route('/books', methods=['GET'])
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True, port=3000)

