#Module for input validation
import book, author, user, genre #import classes for validation
import re

isbn_pattern = r"\d{13}"

#Create a new book
def book_create(library):
    publish_pattern = r"\w{3,} +\d{4}" #Pattern captures a month and a year

    title_inp = input("Please enter the title of the new book you would like to add: ")
    while title_inp == "":
        title_inp = input("Please enter the title of the new book you would like to add: ")
    auth_inp = input("Please enter the name of the author of the book: ")
    while auth_inp == "":
        auth_inp = input("Please enter the author of the book: ")
    isbn_inp = input("Please enter the ISBN of the book you would like to add: ")
    while True:
        if re.match(isbn_pattern, isbn_inp):
            if isbn_inp in library:
                isbn_inp = input("Please enter the unique ISBN of the book: ")
            else:
                break
        else:
            isbn_inp = input("Please enter the ISBN of the book(13 digit unique number): ")
    genre_inp = input("Please enter the genre of the book: ")
    while genre_inp == "":
        genre_inp = input("Please enter the genre of the book: ")
    publish_inp = input("Please enter the publish date of the book: ")
    while True:
        if re.match(publish_pattern, publish_inp):
            break
        else:
            publish_inp = input("Please enter the publish date of the book(Month Year): ")
    
    #if statements to determine if the book needs to be put in a special category
    if genre_inp.lower == "fiction":
        new_book = book.FictionBook(title_inp, auth_inp, isbn_inp, genre_inp, publish_inp)
    elif genre_inp.lower == "mystery":
        new_book = book.MysteryBook(title_inp, auth_inp, isbn_inp, genre_inp, publish_inp)
    elif genre_inp.lower == "nonfiction":
        new_book = book.NonfictionBook(title_inp, auth_inp, isbn_inp, genre_inp, publish_inp)
    else:
        new_book = book.Book(title_inp, auth_inp, isbn_inp, genre_inp, publish_inp)

    #when all input is valid, return the new book object
    return new_book

#Book search function
def book_search(library):
    isbn_input = input("Please enter the ISBN of the book you would like more information on: ")
    while True:
        if re.match(isbn_pattern, isbn_input):
            break
        else:
            isbn_input = input("Please enter the ISBN of the book you would like more information on: ")
    if isbn_input in library:
        return library[isbn_input]
    else:
        return False
    
#Create a new User
def new_user(exist_users):
    id_pattern = r"\d"
    create_user = user.User("", "")
    name_input = input("Please enter the name of the new user: ")
    while name_input == "":
        name_input = input("Please enter the name of the new user: ")
    id_input = input("Please enter a library ID number for the user: ")
    while True:
        if re.match(id_pattern, id_input):
            if id_input in exist_users:
                id_input - input("Please enter a unique numeric library ID: ")
            else:
                break
        else:
            id_input = input("Please enter a valid library ID: ")

    #use setters for name and id
    create_user.set_user_name(name_input)
    create_user.set_library_id(id_input)
    return create_user
    

#Borrow Book Function
def borrow_book(books, users):
    id_pattern = r"\d"

    library_id_input = input("Please enter the user's library ID: ")
    while True:
        if re.match(id_pattern, library_id_input):
            break
        else:
            library_id_input = input("Enter the library ID in a proper format(only numbers): ")
    if library_id_input in users:
        #borrow the book
        book_isbn = input("Please enter the book's ISBN they are borrowing: ")
        while True:
            if re.match(isbn_pattern, book_isbn):
                break
            else:
                book_isbn = input("Please enter the book's ISBN(13 digit number): ")
        if book_isbn in books:
            if books[book_isbn].availability == "Borrowed":
                print("This book is already being borrowed, please try agian.")
            else:
                books[book_isbn].change_availability()
                #add the book to the user's library
                users[library_id_input].add_borrowed_book(books[book_isbn].title)
                print("Book successfully borrowed.")
    else:
        print("Sorry, that is not a valid user.")


#Return book function
def return_book(books, users):
    id_pattern = r"\d"
    library_id_input = input("Please enter the user's library ID: ")
    while True:
        if re.match(id_pattern, library_id_input):
            break
        else:
            library_id_input = input("Please enter the user's library ID: ")

    if library_id_input in users:
        #Return the book
        if users[library_id_input].get_borrowed_books() == []:
            print("This user has not borrowed any books yet.")
        else:
            users[library_id_input].display_borrowed_books()
            book_isbn = input("Please enter the book's ISBN they are returning: ")
            while True:
                if re.match(isbn_pattern, book_isbn):
                    break
                else:
                    book_isbn = input("Please enter the book's ISBN they are returning: ")
            if book_isbn in books:
                if books[book_isbn].availability == "Borrowed" and books[book_isbn].title in users[library_id_input.get_borrowed_books()]:
                    books[book_isbn].change_availability()
                    users[library_id_input].return_borrowed_books(books[book_isbn].title)
                    print("The user's book has been returned.")
                else:
                    print("This book is not being borrowed by the user.")
    else:
        print("This user does not exist in our systems.")


#User search function
def search_user(exist_users):
    id_pattern = r"\d"
    id_input = input("Please enter the ID of the user you would like to view: ")
    while True:
        if re.match(id_pattern, id_input):
            if id_input in exist_users:
                exist_users[id_input].display_user_info()
            else:
                print("The user could not be found, please try again.")
            break
        else:
            id_input = input("Please enter a valid ID")
    
#add Author function
def add_author(exist_author):
    author_name = input("Please enter the name of the new author: ")
    while True or author_name == "":
        if author_name in exist_author:
            author_name = input("Please enter the author's name: ")
        elif author_name == "":
            author_name = input("Please enter the author's name: ")
        else:
            break
    
    author_bio = input("Please enter a short bio of the author: ")
    while author_bio == "":
        author_name = input("Please enter a short bio for the author: ")

    new_author = author.Author(author_name, author_bio)
    return new_author


#Author search function
def search_author(authors):
    find_author = input("Please enter the Author you would like more details on: ")
    while find_author == "":
        find_author = input("Please enter the name of the Author you would like more details on: ")
    if find_author in author:
        authors[find_author].display_author()
    else:
        print("Could not find that author.")

#Add genre function
def add_genre(exist_genre):
    genre_name = input("Please enter the name of the genre: ")
    while True:
        if genre_name in exist_genre:
            genre_name = input("Please enter the name of the genre: ")
        elif genre_name == "":
            genre_name = input("Please enter the name of the genre: ")
        else:
            break
    genre_desc = input("Enter a short description of the genre: ")
    while genre_desc == "":
        genre_desc = input("Please enter a short description of the genre: ")

    genre_cat = input("Please enter the cateogry this genre falls under: ")
    while genre_cat == "":
        genre_cat = input("Please enter the category this genre falls under: ")

    new_genre = genre.Genre(genre_name, genre_desc, genre_cat)
    return new_genre

#Genre search function
def search_genre(exist_genre):
    find_genre = input("Please enter the Genre you would like more details on: ")
    while find_genre == "":
        find_genre = input("Please enter the name of the Genre you would like more details on: ")
    if find_genre in exist_genre:
        exist_genre[find_genre].display_genre()
    else:
        print("Could not find that Genre. Try ading it to the library!")
