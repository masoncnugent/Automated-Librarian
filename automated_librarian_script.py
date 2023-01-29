from books import *
#yeah undo this line below later
from welcome import *
from linkedlist import LinkedList

#creates the linkedlist of linkedlists with book types as the sublists
def insert_book_data():
    book_data_list = LinkedList()
    for book_type in book_types:
        book_sublist = LinkedList()
        for book in book_data:
            if book[0] == book_type:
                book_sublist.insert_beginning(book)
        book_data_list.insert_beginning(book_sublist)

    return book_data_list

#makes the bars that encompass each listed book the length of the greatest extra text and category combination.
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


#creates a sentence from a list with an oxford comma at the end
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


#every question the user could give input on
def questions(id, list):
    if id == 1:
        question = input("\nWhat type of books would you like to read?\nType the first letters of your choosing, with your options being {0}\n".format(list_into_oxford(list)))
    elif id == 2:
        question = input("\nWhat other type of books would you like to read?\nType the first letters of your choosing, with your options being {0}\n".format(list_into_oxford(list)))
    elif id == 3:
        question = input("\nI\'m sorry, it appears you\'ve made an incorrect entry.\nWhat type of books would you like to read?\nType the first letters of your choosing, with your options being {0}\n".format(list_into_oxford(list)))
    elif id == 4:
        question = input("\nI\'m sorry, it appears you\'ve made an incorrect entry.\nWhat other type of books would you like to read?\nType the first letters of your choosing, with your options being {0}\n".format(list_into_oxford(list)))
    elif id == 5:
        question = input("Would you like to search for more books? Type \'y\' for yes or \'n\' for no.\n")
    elif id == 6:
        question = input("\nI\'m sorry, it appears you\'ve made an incorrect entry.\nIf you\'d like to search for more books type \'y\', but if not type \'n\'.\n")
    elif id == 7:
        question = input("\nThe list that match that search are {0}\nType enough letters to narrow down this list.\n".format(list_into_oxford(list)))
    elif id == 8:
        #import dragon_name list so it doesn't cause assignment issues
        question = input("\nBefore we begin, what kind of dragon sounds the most interesting?\nType the first letters of your choosing, with your options being {0}\n".format(list_into_oxford(list)))
    elif id == 9:
        question = input("\nI\'m sorry, it appears you\'ve made an incorrect entry.\nWhat kind of dragon seems the most interesting?\nType the first letters of your choosing, with your options being {0}\n".format(list_into_oxford(list)))
    elif id == 10:
        #just remove the selected dragon from dragon_name_list
        question = input("\nWhat kind of dragon sounds the most frightening? (There\'s three in total.)\nYour options now are {0}\n".format(list_into_oxford(list)))
    elif id == 11:
        question = input("\nI\'m sorry, it appears you\'ve made an incorrect entry.\nWhat kind of dragon sounds the most frightening?\nType the first letters of your choosing, with your options being {0}\n".format(list_into_oxford(list)))
    elif id == 12:
        question = input("\nAnd what will your final dragon be? Choose the most powerful.\nYour remaining options are {0}\n".format(list_into_oxford(list)))
    elif id == 13:
        question = input("\nI\'m sorry, it appears you\'ve made an incorrect entry.\nFor your final dragon, choose the most powerful.\nYour final options are {0}\n".format(list_into_oxford(list)))

    return question


#checks if the users segment is in the book_type from the zeroth index of segment up until its last index
def search_checker(segment, book_type):
    for pointer in range(len(segment)):
        if segment[pointer] != book_type[pointer]:
            return False
    return True


#returns a list of the best possible searches given the user_choice
def match_calculator(user_choice, list):
    possible_item_list = []
    for item in list:
        #this is a better-than-nothing heuristic, but more could be done to limit options than this. The better this heuristic, the less expensive every other operation down the line is. If the dataset were massive, I would prioritize optimizing this
        if item[0] == user_choice[0]:
            possible_item_list.append(item)
    
    #removes any entries shorter in length than the user_choice, so index errors with search_checker() don't occur
    for possible_item in possible_item_list.copy():
        if len(possible_item) < len(user_choice):
            possible_item_list.remove(possible_item)

    if len(possible_item_list) == 0:
        return False

#before comparing best searches there has to be at least one possible match. This also removes non-matches from possible_type_list
    no_match = True
    for possible_item in possible_item_list.copy():
        if search_checker(user_choice, possible_item):
           no_match = False
        elif not search_checker(user_choice, possible_item):
           possible_item_list.remove(possible_item)
    
    if no_match:
        return False

    return decision_maker(possible_item_list)


#recursively calls match_calculator() until the best_choice_list has a length of 1, taking input from the user to narrow this list
def decision_maker(possible_item_list):
    if len(possible_item_list) == 1:
        return possible_item_list[0]
    else:
        #QUESTION 7 WOULD WORK WITH DRAGONS BECAUSE I OVERENGINEERED THAT TOO
        decision = questions(7, possible_item_list)
        return match_calculator(decision, possible_item_list)

    
#calls the helper functions and contains the core logic for when those various functions are called
def main_loop():
    book_data_list = insert_book_data()

    run_val = 1
    user_reset_choice = "y"

    while user_reset_choice == "y":
        user_choice = questions(run_val, book_types)
        match = match_calculator(user_choice)
        while match == False:
            user_choice = questions(run_val + 2, book_types)
            match = match_calculator(user_choice)
        book_details(book_data_list, match)

        user_reset_choice = questions(5, book_types)
        while user_reset_choice != "y" and user_reset_choice != "n":
            user_reset_choice = questions(6, book_types)
        
        if run_val != 2 and user_reset_choice == "y":
            run_val = 2
        else:
            while user_reset_choice != "y" and user_reset_choice != "n":
                user_reset_choice = questions(6, book_types)

    print("\nI hope you found the book(s) you were looking for! Have a nice day!")

def dragon_selector_loop():
    dragons_selected = 0
    run_val = 8
    chosen_dragon_list = []
    while dragons_selected != 3:
        dragon_choice = questions(run_val, dragon_name_list)
        dragon_match = match_calculator(dragon_choice, dragon_name_list)
        while dragon_match == False:
            #add the appropriate error messages two below each dragon message
            dragon_choice = questions(run_val + 1, dragon_name_list)
            dragon_match = match_calculator(dragon_choice, dragon_name_list)
        dragon_index = 0
        #if this gives errors try making the dragon_name_list a .copy()
        for dragon_name in dragon_name_list:
            if dragon_name == dragon_match:
                print("this is dragon_name_list")
                print(dragon_name_list)
                print("dragon_index is currently")
                print(dragon_index)
                print("meaning you have selected")
                print(dragon_name_list[dragon_index])
                print("is that right?")
                #slight discrepancy between name list and dragon list, but they should have identical dragons at their indices
                chosen_dragon_list.append(dragon_list[dragon_index])
                dragons_selected += 1
                run_val += 2
                dragon_name_list.pop(dragon_index)
                dragon_list.pop(dragon_index)
                #make sure this break exits this for loop and not the while loop
                break
            else:
                dragon_index += 1

    print("while loop over, here are the three dragons you've chosen. You'd have to feed them into dragon_printer at this point")

    print("below this should be 3, it's dragons_selected")
    print(dragons_selected)

    print("below this should be 3, it's the length of chosen_dragon_list")
    print(len(chosen_dragon_list))

    print("this should display all your chosen dragons in a broken way")
    for chosen_dragon in chosen_dragon_list:
        print(chosen_dragon)

    print("if that worked, now for the final piece")
    return chosen_dragon_list



#runs every other helper program
def run_program():
    #welcomes the user with some sick dragons, organized dynamically and printed side by side
    print("starting the action")
    chosen_dragon_list = dragon_selector_loop()
    dragon_printer(chosen_dragon_list[0], chosen_dragon_list[1], chosen_dragon_list[2])
    print("action completed")

    #forms the core of the program
    #main_loop()

    #uncomment the above stuff


run_program()