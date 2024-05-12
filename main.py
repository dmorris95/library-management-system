from book import Book, NonfictionBook, FictionBook, MysteryBook
from author import Author
from genre import Genre
from user import User
import input_validators


library = {}
user_library = {}
author_library = {}
genre_library = {}

#Set books and users
book1 = MysteryBook("Cockroaches", "Jo Nesbo", "9780345807151", "Mystery", "January 1998")
book2 = FictionBook("To Kill a Mockingbird", "Harper Lee", "9780446310789", "Fiction", "July 1960")
book3 = NonfictionBook("If I Live Until Morning", "Jean Muenchrath", "9780692955819", "Nonfiction", "March 2018")
book4 = Book("Tigerman", "Nick Harkaway", "9780385352413", "Thriler", "May 2014")
book2.change_availability()

user1 = User("John Smith", "1234")
user2 = User("Steve Johnson", "5123")
user3 = User("Richard James", "1211")
user2.add_borrowed_book("To Kill a Mockingbird")

library[book1.isbn] = book1
library[book2.isbn] = book2
library[book3.isbn] = book3
library[book4.isbn] = book4

user_library[user1.get_library_id()] = user1
user_library[user2.get_library_id()] = user2
user_library[user3.get_library_id()] = user3

#set authors and genres
author1 = Author("Jo Nesbo", "Norwegian Author who has a series of detective novels about Harry Hole.")
author2 = Author("Dr. Suess", "The Rhyme Guy")
author3 = Author("Harper Lee", "Old school author who writes about touchy subjects")

author_library[author1.name] = author1
author_library[author2.name] = author2
author_library[author3.name] = author3

genre1 = Genre("Fantasy", "Magical things happen here.", "Fiction")
genre2 = Genre("Thriller", "Keeping you on your toes with so many twists and turns.", "Fiction")
genre3 = Genre("Biography", "Story about someone's life", "Nonfiction")

genre_library[genre1.name] = genre1
genre_library[genre2.name] = genre2
genre_library[genre3.name] = genre3


def menu_display():
    try:
        menu_choice = 0
        print("Welcome to the Library Management System!")
        while menu_choice != 5:
            menu_choice = menu_input()
    except Exception as e:
        print(e)
    finally:
        print("Thank you for using the Library Management System!")


def menu_input():

    try:
        main_menu_string = "1. Book Operations\n2. User Operations\n3. Author Operations\n4. Genre Operations\n5. Quit"
        print("Main Menu:")
        print (main_menu_string)
        user_choice = int(input("Please enter the number of the option you would like to perform: "))

        #Book Operations
        if user_choice == 1:
            print("Book Operations: ")
            print("1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book by ISBN\n5. Display all books")
            book_choice = int(input("Please enter the number of the option you would like to select: "))
            if book_choice == 1: #Add a book
                new_book = input_validators.book_create(library)
                library[new_book.isbn] = new_book
                print("Book successfully added!")

            elif book_choice == 2: #Borrow a book
                input_validators.borrow_book(library, user_library)

            elif book_choice == 3: #Return a book
                input_validators.return_book(library, user_library)   

            elif book_choice == 4: #Search for a book by isbn
                found_book = input_validators.book_search(library)
                if found_book == False:
                    print("The book could not be found in our library.")
                else:
                    print (found_book)
                    
            elif book_choice == 5: #Display all books
                for b, b_info in library.items():
                    print("ISBN:", b, "Title:", b_info.title)

        #User Operations
        elif user_choice == 2:
            print("User Operations: ")
            print("1. Add a new user\n2. View user details\n3. Display all users")
            user_oper_choice = int(input("Please enter the number of the option you would like to select: "))
            if user_oper_choice == 1:
                new_use = input_validators.new_user(user_library)
                user_library[new_use.get_library_id()] = new_use
                print("User successfully added!")
            elif user_oper_choice == 2:
                input_validators.search_user(user_library)
                
            elif user_oper_choice == 3:
                for usr, usr_info in user_library.items():
                    print(f"Library ID: {usr} ---- Name: {usr_info.get_user_name()}")

        #Author Operations    
        elif user_choice == 3:
            print("Author Operations: ")
            print("1. Add a new author\n2. View author details\n3. Display all authors")
            author_choice = int(input("Please enter the number of the option you would like to select: "))
            if author_choice == 1: #Add an Author 
                new_author = input_validators.add_author(author_library)
                author_library[new_author.name] = new_author
                print("Author successfully added!")
            elif author_choice == 2: #Search for an Author
                input_validators.search_author(author_library)
            elif author_choice == 3: #Display list of Authors
                print("Authors in the library: ")
                for auths in author_library:
                    print(auths)

        #Genre Operations    
        elif user_choice == 4:
            print("Genre Operations: ")
            print("1. Add a new genre\n2. View genre details\n3. Display all genres")
            genre_choice = int(input("Please enter the number of the option you would like to select: "))
            if genre_choice == 1: #add genre
                new_genre = input_validators.add_genre(genre_library)
                genre_library[new_genre.name] = new_genre
                print("Genre successfully added!")
            elif genre_choice == 2: #search for a specific genre
                input_validators.search_genre(genre_library)
            elif genre_choice == 3: #Display list of Genres
                print("Genres in the library: ")
                for genres in genre_library:
                    print(genres)

        elif user_choice == 5:
            return user_choice
        else:
            raise ValueError()
    except ValueError:
        print("Please enter a valid number choice")
        menu_display()

menu_display()