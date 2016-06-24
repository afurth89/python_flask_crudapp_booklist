class Book():
  id = 1

  def __init__(self, title, author):
    self.title = title
    self.author = author
    self.id = Book.id
    Book.id += 1