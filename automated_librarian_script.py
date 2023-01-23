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

def bar_maker(current_book):
    bar_length = 0
    for i in range(1, 6):

        if i == 1:
            extra = len("Title: ")
        elif i == 2:
            extra = len("Author: ")
        elif i == 3:
            extra = len("Year Written: ")
        elif i == 4:
            extra = len("Critic Review: ")
        elif i == 5:
            extra = len("User Review")

        if len(current_book.get_value()[i]) + extra > bar_length:
            bar_length = len(current_book.get_value()[i]) + extra
        
    bar = ""
    for bar_addition in range(0, bar_length):
        bar += "="
    return bar

#prints out the details of every book that matches the type of book the user has searched for
def book_details(book_data_list, match):
    current_list = book_data_list.get_head_node()
    while current_list.get_value():
        current_book = current_list.get_value().get_head_node()
        if match == current_book.get_value()[0]:
            print("\nDisplaying books from the category " + match + ".\n")
            while current_book.get_value():
                bar = bar_maker(current_book)

                print(bar)
                print("Title: " + current_book.get_value()[1]) 
                print("Author: " + current_book.get_value()[2])
                print("Year Written: " + current_book.get_value()[3])
                print("Critic Review: " + current_book.get_value()[4])
                print("User Review: " + current_book.get_value()[5])
                print(bar)
                print("")
                current_book = current_book.get_next_node()
            current_list = current_list.get_next_node()
        else:
            current_list = current_list.get_next_node()


#creates a sentence of the book types with an oxford comma at the end
def book_type_oxford(types):
    oxford_sentence = ""
    pointer = 0
    if len(types) > 2:
        while pointer != len(types) - 1:
            oxford_sentence += types[pointer] + ", "
            pointer += 1
    elif len(types) == 2:
        oxford_sentence += types[pointer] + " "
        pointer += 1
    oxford_sentence += "and " + types[pointer] + "."
    return oxford_sentence


#every question the user could give input on
def questions(id, types=types):
    if id == 1:
        question = input("\nWhat type of books would you like to read?\nType the first letters of your choosing, with your options being {0}\n".format(book_type_oxford(types)))
    elif id == 2:
        question = input("\nWhat other type of books would you like to read?\nType the first letters of your choosing, with your options being {0}\n".format(book_type_oxford(types)))
    elif id == 3:
        question = input("\nI\'m sorry, it appears you've made an incorrect entry.\nWhat type of books would you like to read?\nType the first letters of your choosing, with your options being {0}\n".format(book_type_oxford(types)))
    elif id == 4:
        question = input("\nI\'m sorry, it appears you've made an incorrect entry.\nWhat other type of books would you like to read?\nType the first letters of your choosing, with your options being {0}\n".format(book_type_oxford(types)))
    elif id == 5:
        question = input("Would you like to search for more books? Type \'y\' for yes or \'n\' for no.\n")
    elif id == 6:
        question = input("\nI\'m sorry, it appears you've made an incorrect entry.\nIf you'd like to search for more books type \'y\', but if not type \'n\'.\n")
    elif id == 7:
        question = input("\nThe types that match that search are {0}\nType enough letters to narrow down this list.\n".format(book_type_oxford(types)))

    return question


#checks if the users segment is in the book_type from the zeroth index of segment up until its last index
def search_checker(segment, book_type):
    for pointer in range(len(segment)):
        if segment[pointer] != book_type[pointer]:
            return False
    return True


#returns a list of the best possible searches given the user_choice
def match_calculator(user_choice, types=types):
    possible_type_list = []
    for type in types:
        #this is a better-than-nothing heuristic, but more could be done to limit options than this. The better this heuristic, the less expensive every other operation down the line is. If the dataset were massive, I would prioritize optimizing this
        if type[0] == user_choice[0]:
            possible_type_list.append(type)
    
    #removes any entries shorter in length than the user_choice, so index errors with search_checker() don't occur
    for possible_type in possible_type_list.copy():
        if len(possible_type) < len(user_choice):
            possible_type_list.remove(possible_type)

    if len(possible_type_list) == 0:
        return False

#before comparing best searches there has to be at least one possible match. This also removes non-matches from possible_type_list
    no_match = True
    for possible_type in possible_type_list.copy():
        if search_checker(user_choice, possible_type):
           no_match = False
        elif not search_checker(user_choice, possible_type):
           possible_type_list.remove(possible_type)
    
    if no_match:
        return False

    return decision_maker(possible_type_list)


#recursively calls match_calculator() until the best_choice_list has a length of 1, taking input from the user to narrow this list
def decision_maker(possible_type_list):
    if len(possible_type_list) == 1:
        return possible_type_list[0]
    else:
        decision = questions(7, possible_type_list)
        return match_calculator(decision, possible_type_list)

    
#calls the helper functions and contains the core logic for when those various functions are called
def main_loop():
    book_data_list = insert_book_data()

    run_val = 1
    user_reset_choice = "y"

    while user_reset_choice == "y":

        user_choice = questions(run_val)
        match = match_calculator(user_choice)
        while match == False:
            user_choice = questions(run_val + 2)
            match = match_calculator(user_choice)
        book_details(book_data_list, match)

        user_reset_choice = questions(5)
        while user_reset_choice != "y" and user_reset_choice != "n":
            user_reset_choice = questions(6)
        
        if run_val != 2 and user_reset_choice == "y":
            run_val = 2
        else:
            while user_reset_choice != "y" and user_reset_choice != "n":
                user_reset_choice = questions(6)

    print("\nI hope you found the book(s) you were looking for! Have a nice day!")


def run_program():
    #welcomes the user with some sick dragons, organized dynamically and printed side by side
    dragon_printer(dragon_scary, dragon_aloofy, dragon_goofy)

    main_loop()


run_program()

#some of the dragons might be messed up compared to their online versions