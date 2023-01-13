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

#prints out the details of every book that matches the type of book the user has searched for
def book_details(book_data_list, match):
    current_list = book_data_list.get_head_node()
    while current_list.get_value():
        current_book = current_list.get_value().get_head_node()
        if match == current_book.get_value()[0]:
            while current_book.get_value():
                print("================================")
                print("Title: " + current_book.get_value()[1]) 
                print("Author: " + current_book.get_value()[2])
                print("Year Written: " + current_book.get_value()[3])
                print("Critic Review: " + current_book.get_value()[4])
                print("User Review: " + current_book.get_value()[5])
                print("================================")
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
        question = input("I\'m sorry, it appears you've made an incorrect entry.\n If you'd like to search for more books type \'y\', but if not type \'n\'.")
    elif id == 7:
        question = input("\nThe types that match that search are {0}\nType the first letters of your choosing to narrow down this list.\n".format(book_type_oxford(types)))

    return question


#checks if the users search is in the only remaining book type fom the start of the search segment up until the type word
def search_checker(segment, word):
    for pointer in range(len(segment)):
        if segment[pointer] != word[pointer]:
            print(segment + " not in " + word + " from beginning of word up until end of segment")
            return False
    return True


#returns a list of the best possible searches given the user_choice
def match_calculator(user_choice, types=types):
    possible_type_list = []
    for type in types:
        #this is a better-than-nothing heuristic, but more could be done to limit options than this. The better this heuristic, the less expensive every other operation down the line is. If the dataset were massive, I would prioritize optimizing this
        if type[0] == user_choice[0]:
            possible_type_list.append(type)
    
    #hmm how to remove entries that start off matching but deviate later, while avoiding entries that match halfway through but not at the beginning... with protections for segments longer than words

    if len(possible_type_list) == 0:
        return False
    elif len(possible_type_list) == 1:
        #an effort at the simpler checking system, which would solve the problem of the above comment
        if search_checker(user_choice, possible_type_list[0]):
            return possible_type_list[0]
        else:
            return False

    print("\nbelow this is/are the possible type(s)")
    print(possible_type_list)
    print("")

    score_list = []
    for possible_type in possible_type_list:
        score = 0
        for i in range(0, len(user_choice)):
            if user_choice[i] == possible_type[i]:
                score += 1
            #what would happen if the user_choice was longer than possible_type, or had a break in it's characters which matched, either of which should disqualify it from consideration?
        score_list.append(score)

    print("below this is the score_list")
    print(score_list)
    print("")

    max_score = 0
    best_choice_list = []
    for i in range(0, len(score_list)):
        if score_list[i] > max_score:
            #there is likely a one line solution to the two lines below
            best_choice_list.clear()
            best_choice_list.append(possible_type_list[i])
            max_score = score_list[i]

        elif score_list[i] == max_score:
            best_choice_list.append(possible_type_list[i])

    print("below this is/are the best search choice(s)")
    print(best_choice_list)

    return decision_maker(best_choice_list)

#recursively calls match_calculator until the best_choice_list has a length of 1, taking input from the user to narrow this list
def decision_maker(best_choice_list):
    if len(best_choice_list) == 1:
        return best_choice_list[0]
    else:
        decision = questions(7, best_choice_list)
        return match_calculator(decision, best_choice_list)

    
#calls the helper functions and contains the core logic for when those various functions are called
def main_loop():
    book_data_list = insert_book_data()

    run_state = 0
    user_reset_choice = "y"

    while user_reset_choice == "y":
        if run_state == 0:
            user_choice = questions(1)
            match = match_calculator(user_choice)
            while match == False:
                user_choice = questions(3)
                match = match_calculator(user_choice)
            book_details(book_data_list, match)

            user_reset_choice = questions(5)
            while user_reset_choice != "y" and user_reset_choice != "n":
                user_reset_choice = questions(6)
            
            if user_reset_choice == "y":
                run_state = 1

        #this is the run state where the user has asked to see more books. in this case, the dialogue is different to reflect that change
        elif run_state == 1:
            user_choice = questions(2)
            match = match_calculator(user_choice)
            while match == False:
                user_choice = questions(4)
                match = match_calculator(user_choice)
            book_details(book_data_list, match)

            user_reset_choice = questions(5)
            while user_reset_choice != "y" and user_reset_choice != "n":
                user_reset_choice = questions(6)


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