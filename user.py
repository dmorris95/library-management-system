
class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.borrowed_books = []
    
    def get_user_name(self):
        return self.__name
    def set_user_name(self, user_name):
        self.__name = user_name

    def get_library_id(self):
        return self.__library_id
    def set_library_id(self, lib_id):
        self.__library_id = lib_id
    
    def get_borrowed_books(self):
        return self.borrowed_books

    def display_borrowed_books(self):
        if self.borrowed_books == []:
            print("This user does not have any books checked out right now.")
        else:
            print("The user currently has the following books being borrowed: ")
            for title in self.borrowed_books:
                print(title)
    
    def display_user_info(self):
        print(f"Library ID: {self.get_library_id()}\nName: {self.get_user_name()}")
        self.display_borrowed_books()
    
    def add_borrowed_book(self, title):
        self.borrowed_books.append(title)
    def return_borrowed_book(self, title):
        self.borrowed_books.remove(title)


