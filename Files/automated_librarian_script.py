from books import *
from welcome import *
from creatures import *
from linkedlist import LinkedList
import random

#Creates the linkedlist of linkedlists with book types as the sublists.
#I used linkedlists because it was part of the coding exercise on Codecademy. Yes, lists would be easier, but this demonstrates a fundamental understanding of what the 'list' data structure is.
def insert_book_data():
    book_data_list = LinkedList()
    for book_type in book_types:
        book_sublist = LinkedList()
        for book in book_data:
            if book[0] == book_type:
                book_sublist.insert_beginning(book)
        book_data_list.insert_beginning(book_sublist)

    return book_data_list

#Makes the bars that encompass each listed book the length of the greatest default text and category name combination.
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


#Prints out the details of every book that matches the type of book the user has searched for.
def book_details(book_data_list, match, x_line_length):
    current_list = book_data_list.get_head_node()
    while current_list.get_value():
        current_book = current_list.get_value().get_head_node()
        if match == current_book.get_value()[0]:
            print("\nDisplaying books from the category " + match + ".\n\n")
            #This part makes a boundary for all the categories based on the length of title_total_length
            x_line = ""
            for i in range(0, x_line_length):
                x_line += "x"
            print(x_line + "\n")
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
    print(x_line)
    print("\n")


#Creates a sentence from a list with an oxford comma at the end.
def list_into_oxford(list):
    oxford_sentence = ""
    pointer = 0

    if len(list) == 1:
        return list[pointer] + "."
    elif len(list) > 2:
        while pointer != len(list) - 1:
            oxford_sentence += list[pointer] + ", "
            pointer += 1
    elif len(list) == 2:
        oxford_sentence += list[pointer] + " "
        pointer += 1
    oxford_sentence += "and " + list[pointer] + "."
    return oxford_sentence


#Every question the user could give input on.
def questions(id, list):
    if id == 1:
        question = input("\n\nWhat type of books would you like to read?\nType the first letters of your choosing, with your options being {0}\n".format(list_into_oxford(list)))
    elif id == 2:
        question = input("\n\nWhat other type of books would you like to read?\nType the first letters of your choosing, with your options being {0}\n".format(list_into_oxford(list)))
    elif id == 3:
        question = input("\n\nI\'m sorry, it appears you\'ve made an incorrect entry.\nWhat type of books would you like to read?\nType the first letters of your choosing, with your options being {0}\n".format(list_into_oxford(list)))
    elif id == 4:
        question = input("\n\nI\'m sorry, it appears you\'ve made an incorrect entry.\nWhat other type of books would you like to read?\nType the first letters of your choosing, with your options being {0}\n".format(list_into_oxford(list)))
    elif id == 5:
        question = input("Would you like to search for more books? Type \'y\' for yes or \'n\' for no.\n")
    elif id == 6:
        question = input("\n\nI\'m sorry, it appears you\'ve made an incorrect entry.\nIf you\'d like to search for more books type \'y\', but if not type \'n\'.\n")
    elif id == 7:
        question = input("\nThe list that match that search are {0}\nType enough letters to narrow down this list.\n".format(list_into_oxford(list)))
    elif id == 8:
        question = input("Before we begin, what kind of creature sounds the most interesting?\nType the first letters of your choosing. Your options are {0}\n".format(list_into_oxford(list)))
    elif id == 9:
        question = input("\n\nI\'m sorry, it appears you\'ve made an incorrect entry.\nWhat kind of creature seems the most interesting?\nType the first letters of your choosing, with your options being {0}\n".format(list_into_oxford(list)))
    elif id == 10:
        question = input("\n\nWhat kind of creature sounds the most frightening? (There\'s three in total.)\nType the first letters of your choosing. Your options now are {0}\n".format(list_into_oxford(list)))
    elif id == 11:
        question = input("\n\nI\'m sorry, it appears you\'ve made an incorrect entry.\nWhat kind of creature sounds the most frightening?\nType the first letters of your choosing, with your options being {0}\n".format(list_into_oxford(list)))
    elif id == 12:
        question = input("\n\nAnd what will your final creature be? Choose the most powerful.\nType the first letters of your choosing. Your remaining options are {0}\n".format(list_into_oxford(list)))
    elif id == 13:
        question = input("\n\nI\'m sorry, it appears you\'ve made an incorrect entry.\nFor your final creature, choose the most powerful.\nType the first letters of your choosing, with your final options being {0}\n".format(list_into_oxford(list)))

    return question


#Checks if the users segment is in the possible_item from the zeroth index of segment up until its last index. possible_item denotes that the item has not yet been determined to be what the user searched for, but rather that it is a potential search option.
def search_checker(segment, possible_item):
    for pointer in range(len(segment)):
        if segment[pointer] != possible_item[pointer]:
            return False
    return True


#returns a list of the best possible searches given the user_choice
def match_calculator(user_choice, list):
    possible_item_list = []
    for item in list:
        #This is a better-than-nothing heuristic, but more could be done to limit options than this. The better this heuristic, the less expensive every other operation down the line is. If the dataset were massive, I would prioritize optimizing this.
        if item[0] == user_choice[0]:
            possible_item_list.append(item)
    
    #Removes any entries shorter in length than the user_choice, so index errors with search_checker() don't occur.
    for possible_item in possible_item_list.copy():
        if len(possible_item) < len(user_choice):
            possible_item_list.remove(possible_item)

    if len(possible_item_list) == 0:
        return False

#Before comparing best searches there has to be at least one possible match. This also removes non-matches from possible_item_list.
    no_match = True
    for possible_item in possible_item_list.copy():
        if search_checker(user_choice, possible_item):
           no_match = False
        elif not search_checker(user_choice, possible_item):
           possible_item_list.remove(possible_item)
    
    if no_match:
        return False

    return decision_maker(possible_item_list)


#Recursively calls match_calculator() until the possible_item_list has a length of 1, taking input from the user to narrow this list. 
#If the user inputs a non-matching search, the narrowing process is ended and the larger list is presented back to the user. 
#More work could have been done to keep the user on the narrowed options until a successful search is made, with an additional way to back out into the larger list, but this would be even more control flow than this project already has.
def decision_maker(possible_item_list):
    if len(possible_item_list) == 1:
        return possible_item_list[0]
    else:
        #questions(7) is one of the few to work with both books and creatures
        decision = questions(7, possible_item_list)
        return match_calculator(decision, possible_item_list)

    
#Calls the helper functions and contains the core logic for when those various functions are called and what to save their returned values as.
def main_loop(x_line_length):
    book_data_list = insert_book_data()

    run_val = 1
    user_reset_choice = "y"

    while user_reset_choice == "y":
        user_choice = questions(run_val, book_types)
        match = match_calculator(user_choice, book_types)
        while match == False:
            user_choice = questions(run_val + 2, book_types)
            match = match_calculator(user_choice, book_types)
        book_details(book_data_list, match, x_line_length)

        user_reset_choice = questions(5, book_types)
        while user_reset_choice != "y" and user_reset_choice != "n":
            user_reset_choice = questions(6, book_types)
        
        if run_val != 2 and user_reset_choice == "y":
            run_val = 2
        else:
            while user_reset_choice != "y" and user_reset_choice != "n":
                user_reset_choice = questions(6, book_types)

    print("\nI hope you found the book(s) you were looking for! Have a nice day!")

#Allows the user to select the creatures (there used to be general creatures but the Pokémon art was so clean it became exclusively Pokémon) that they want. They aren't yet ordered for how they'll be printed
def creature_selector_loop():
    creatures_selected = 0
    run_val = 8
    chosen_creature_list = []

    while creatures_selected != 3:
        creature_choice = questions(run_val, creature_name_list)
        creature_match = match_calculator(creature_choice, creature_name_list)

        while creature_match == False:
            creature_choice = questions(run_val + 1, creature_name_list)
            creature_match = match_calculator(creature_choice, creature_name_list)
        print("\nAdding " + creature_match + " to the list of creatures...\n")
        creature_index = 0

        for creature_name in creature_name_list:
            if creature_name == creature_match:
                chosen_creature_list.append(creature_list[creature_index])
                creatures_selected += 1
                run_val += 2
                creature_name_list.pop(creature_index)
                creature_list.pop(creature_index)
                break
            else:
                creature_index += 1
    #These newlines could have been in a number of places before the creatures are printed. They give some space for the creatures to breathe.
    print("\n\n")
    return chosen_creature_list

#Selects the creatures for the welcome screen based on random number generation instead of user input.
def random_creature_selector():
    creatures_selected = 0
    chosen_creature_list = []
    while creatures_selected < 3:
        random_choice = random.choice(creature_list)
        chosen_creature_list.append(random_choice)
        creature_list.remove(random_choice)
        creatures_selected += 1
    return chosen_creature_list

#Runs everything inside of it. See referenced functions for their comments.
def run_program():
    #This is the user chosen version of selecting the greeting creatures.
    chosen_creature_list = creature_selector_loop()

    #This is the randomized version of selecting the greeting creatures. There are 969 different starting combinations.
    #chosen_creature_list = random_creature_selector()

    #The important part here is that creature_printer() runs, NOT that the returned value is saved to be used for formatting the x_line surrounding the printed books.
    x_line_length = creature_printer(chosen_creature_list[0], chosen_creature_list[1], chosen_creature_list[2])

    #In an ideal world, x_line_length would be reused to determine the length of the terminal window that the resulting program would run in, so everything formats perfectly.
    main_loop(x_line_length)


run_program()