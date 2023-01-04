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

#creates the linkedlist of linkedlists with book types as the sublist lists
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
    pass


#this determines what genre the user has chosen and prints all its books to the console.
def genre_printer(book_data_list, user_letter_choice):
    current_list = book_data_list.get_head_node()
    while current_list.get_value():
        current_genre = current_list.get_value().get_head_node().get_value()[0]
        #eventually include a possibility checker where the user can make a multi-character string and all of that will be compared against the first letters of the categories. The one with the most consecutive matches is your choice, and if multiple matches exist they are presented to the user as a choice.
        if user_letter_choice == current_genre[0]:
            print("\nHere is a list of " + current_genre + " books:")
            print(current_list.get_value().stringify_list())
            break
        else:
            current_list = current_list.get_next_node()


def book_type_oxford(types):
    oxford_sentence = ""
    pointer = 0
    while pointer != len(types) - 1:
        oxford_sentence += types[pointer] + ", "
        pointer += 1
    oxford_sentence += "and " + types[pointer] + "."
    return oxford_sentence

def book_type_prefixes(types):
    prefix_list = []
    pointer = 0
    while pointer != len(types):
        prefix_list.append(types[pointer][0])
    return prefix_list


def main_loop(book_data_list):
    run_state = 0
    user_reset_choice = False
    user_reset_choice_question = "Would you like to search for more books? Type \'y\' for yes or \'n\' for no.\n"
    while not user_reset_choice:
        if run_state == 0:
            user_letter_choice = input("What type of books would you like to read?\nType the first letters of your choosing, with your options being {0}\n".format(book_type_oxford(types)))
            #add logic to test if user_letter_choice is actually in the book_type_prefixes(types). You could make this smarter so it combs through the start of each type to see which type it has the most matches for...

            genre_printer(book_data_list, user_letter_choice)
            user_reset_choice = input(user_reset_choice_question)
            while user_reset_choice != "y" or user_reset_choice != "n":
                user_reset_choice = input(user_reset_choice_question)
                print(user_reset_choice)
            #figure out how to not need these break statements. they shouldn't be needed...
            if user_reset_choice == "y":
                run_state = 1
                break
            elif user_reset_choice == "n":
                user_reset_choice = True
                print(user_reset_choice)
                break

        elif run_state == 1:
            user_letter_choice = input("What other type of books would you like to read?\nType the first letters of your choosing, with your options being {0}\n".format(book_type_oxford(types)))
            genre_printer(book_data_list, user_letter_choice)


    print("I hope you found the book(s) you were looking for! Have a nice day!")





def run_program():
    #this book_type_list isn't actually in use yet...
    #insert_book_types()

    book_data_list = insert_book_data()

    #do an introductory step and then the main loop

    main_loop(book_data_list)
    print(book_type_prefixes(types))
        
run_program()