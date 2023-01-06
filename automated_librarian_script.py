from books import *
from welcome import *
from linkedlist import LinkedList


#creates the linkedlist of linkedlists with book types as the sublists
def insert_book_data():
    book_data_list = LinkedList()
    for book_type in types:
        book_sublist = LinkedList()
        for book in book_data:
            if book[0] == book_type:
                book_sublist.insert_beginning(book)
        book_data_list.insert_beginning(book_sublist)

    return book_data_list


#this determines what genre the user has chosen and prints all its books to the console
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


#creates a sentence of the book types with an oxford comma at the end
def book_type_oxford(types):
    oxford_sentence = ""
    pointer = 0
    while pointer != len(types) - 1:
        oxford_sentence += types[pointer] + ", "
        pointer += 1
    oxford_sentence += "and " + types[pointer] + "."
    return oxford_sentence

#looks through types and makes a list of all the letter prefixes of the types. this might be refactored entirely so strings of starting characters of the types can be compared, as a more sophisticated search
def book_type_prefixes(types):
    prefix_list = []
    pointer = 0
    while pointer != len(types):
        prefix_list.append(types[pointer][0])
        pointer += 1
    return prefix_list

#returns True if the user chose a letter that is one of the prefixes within the types list
def prefix_checker(user_letter_choice, prefix_list):
    if user_letter_choice in prefix_list:
        return True
    return False

#calls the helper functions and contains the core logic for when those various functions are called
def main_loop():
    book_data_list = insert_book_data()

    run_state = 0
    user_reset_choice = "y"
    user_reset_choice_question = "Would you like to search for more books? Type \'y\' for yes or \'n\' for no.\n"
    while user_reset_choice == "y":
        if run_state == 0:
            user_letter_choice = input("What type of books would you like to read?\nType the first letters of your choosing, with your options being {0}\n".format(book_type_oxford(types)))
            if prefix_checker(user_letter_choice, book_type_prefixes(types)):
                genre_printer(book_data_list, user_letter_choice)
            else:
                while not prefix_checker(user_letter_choice, book_type_prefixes(types)):
                    user_letter_choice = input("\nI'm sorry, it appears you've made a incorrect entry.\nType the first letters of your choosing, with your options being {0}\n".format(book_type_oxford(types)))
                genre_printer(book_data_list, user_letter_choice)

            user_reset_choice = input(user_reset_choice_question)
            while user_reset_choice != "y" and user_reset_choice != "n":
                user_reset_choice = input(user_reset_choice_question)
            
            if user_reset_choice == "y":
                run_state = 1

        #this is the run state where the user has asked to see more books. in this case, the dialogue is different to reflect that change
        elif run_state == 1:
            user_letter_choice = input("\nWhat other type of books would you like to read?\nType the first letters of your choosing, with your options being {0}\n".format(book_type_oxford(types)))
            if prefix_checker(user_letter_choice, book_type_prefixes(types)):
                genre_printer(book_data_list, user_letter_choice)
            else:
                while not prefix_checker(user_letter_choice, book_type_prefixes(types)):
                    user_letter_choice = input("\nI'm sorry, it appears you've made a incorrect entry.\nType the first letters of your choosing, with your options being {0}\n".format(book_type_oxford(types)))
                genre_printer(book_data_list, user_letter_choice)

            user_reset_choice = input(user_reset_choice_question)
            while user_reset_choice != "y" and user_reset_choice != "n":
                user_reset_choice = input(user_reset_choice_question)


    print("\nI hope you found the book(s) you were looking for! Have a nice day!")




def run_program():
    #print_welcome()

    main_loop()
        
#additional stuff to add:
"""
make it so that the user can select a specific book, which should print out a sentence detailing it's name, author, critic and user reviews.
you could make it so that searches are true searches with a conflict message asking the user to make a choice if two or more options match the multi-character prefix string the user gave.
finish print_welcome, of course.
fill out book_data
"""

run_program()