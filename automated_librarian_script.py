from books import *
from welcome import *
from linkedlist import LinkedList

#print_welcome()

#makes a linkedlist of all the book types
def insert_book_types():
    book_type_list = LinkedList()
    for book_type in types:
        book_type_list.insert_beginning(book_type)
    print(book_type_list.stringify_list())
    print("done with this section\n")
    return book_type_list

def insert_book_data():
    book_data_list = LinkedList()
    for book_type in types:
        book_sublist = LinkedList()
        for book in book_data:
            if book[0] == book_type:
                book_sublist.insert_beginning(book)
        book_data_list.insert_beginning(book_sublist)

    return book_data_list

def get_user_choices():
    print("see if you can abstract some choice gathering to here")

def run_program():
    #this book_type_list isn't actually in use yet...
    #insert_book_types()
    book_data_list = insert_book_data()

    user_letter_choice = input("What type of book would you like to read?\nType \'p\' for philosophical, \'c\' for comic strip, \'a\' for adventure, or \'e\' for english curriculum\n")

    #this determines what genre the user has chosen
    current_list = book_data_list.get_head_node()
    while current_list.get_value():
        current_genre = current_list.get_value().get_head_node().get_value()[0]
        if user_letter_choice == current_genre[0]:
            print("\nHere is a list of " + current_genre + " books:")
            print(current_list.get_value().stringify_list())
            break
        else:
            current_list = current_list.get_next_node()


run_program()