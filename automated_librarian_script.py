from books import *
from welcome import *
from linkedlist import LinkedList

#print_welcome()

#makes a linkedlist of all the book types
def insert_book_types():
    book_type_list = LinkedList()
    for book_type in types:
        print(book_type)
        book_type_list.insert_beginning(book_type)
    #print(book_type_list.stringify_list())
    book_type_list.simple_should_work()
    return book_type_list

def insert_book_data():
    book_data_list = LinkedList()
    for book_type in types:
        book_sublist = LinkedList()
        for book in book_data:
            if book[0] == book_type:
                book_sublist.insert_beginning(book)
        print(book_sublist.stringify_list())
        book_data_list.insert_beginning(book_sublist)
        return book_data_list
    
#print(insert_book_data().stringify_list())

insert_book_types()

#insert_book_data()


