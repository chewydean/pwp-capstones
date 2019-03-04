class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("This user's email has been updated.")

    def __repr__(self):
        return "User {name}, email: {email}, books read: {books}".format(name = self.name, email = self.email, books = len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False
    
    def read_book(self, book, rating=0):
        self.books[book] = rating

    def get_average_rating(self):
        result = 0
        for book in self.books.values():
            result += book
        final = result / len(self.books)
        return final


class Book(object):
    def __init__(self, title, isbn, price=0):
        self.title = title
        self.isbn = isbn
        self.ratings = []
        self.price = price

    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, isbn):
        self.isbn = isbn
        print("This book's ISBN has been updated.")

    def add_rating(self, rating):
        if rating != "None":
            if rating >= 0 and rating <= 4:
                self.ratings.append(rating)
            else:
                print("Invalid Rating")
        else:
            self.ratings.append(rating)

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False
    
    def get_average_rating(self):
        result = 0
        for book in self.ratings:
            result += book
        final = result / len(self.ratings)
        return final

    def __hash__(self):
        return hash((self.title, self.isbn))

class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=0):
        user = self.users.get(email)
        if user:
            user.read_book(book, rating)
            book.add_rating(rating)
            if self.books.get(book):
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email {email}!".format(email = email))

    def add_user(self, name, email, user_books="None"):
        name = User(name, email)
        self.users[email] = name
        if user_books != "None":
            for book in user_books:
                self.add_book_to_user(book, email)
    
    def print_catalog(self):
        for book in self.books.keys():
            print(book)
    
    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        lst = []
        for item in self.books.keys():
            lst.append(item)
        lst.sort(key = self.books.__getitem__)
        return lst[0]
    
    def highest_rated_book(self):
        result = 0
        curr = ""
        for book in self.books:
            if book.get_average_rating() > result:
                result = book.get_average_rating()
                curr = book
        return curr

    def most_positive_user(self):
        result = 0
        curr = ""
        for user in self.users.values():
            if user.get_average_rating() > result:
                result = user.get_average_rating()
                curr = user
        return curr

    def get_n_most_expensive_books(self, n):
        lst = []
        for item in self.books.keys():
            lst.append(item)
        lst.sort(key = item.price)
        return lst[:n - 1]

    def get_worth_of_user(self, user_email):
        worth = 0
        user = self.users.get(user_email)
        for book in user.books:
            worth += book.price
        return worth

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author
    
    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)
    
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)