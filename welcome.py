def print_welcome():
    print("use this later!")

def dragon_metadata_maker(dragon):
    dragon_data = []
    dragon_line_list = dragon.splitlines()
    for line in dragon_line_list:
        dragon_data.append(len(line))
    #the line below this gets rid of the newline that exists at the start of each dragon because of where the """ marks start
    dragon_data.pop(0)
    dragon_x = max(dragon_data)
    dragon_y = len(dragon_data)
    return dragon_data, dragon_x, dragon_y

def dragon_printer(dragon_1, dragon_2, dragon_3):
    dragon_1_metadata = dragon_metadata_maker(dragon_1)
    dragon_2_metadata = dragon_metadata_maker(dragon_2)
    dragon_3_metadata = dragon_metadata_maker(dragon_3)
    print(dragon_1_metadata)
    print(dragon_2_metadata)
    print(dragon_3_metadata)

    possible_max_x_list = []
    possible_max_x_list.append(dragon_1_metadata[1])
    possible_max_x_list.append(dragon_2_metadata[1])
    possible_max_x_list.append(dragon_3_metadata[1])
    max_x = max(possible_max_x_list)
    print("this is the largest x value")
    print(max_x)

    possible_max_y_list = []
    possible_max_y_list.append(dragon_1_metadata[2])
    possible_max_y_list.append(dragon_2_metadata[2])
    possible_max_y_list.append(dragon_3_metadata[2])

    max_y = max(possible_max_y_list)
    print("this is the largest y value")
    print(max_y)

    print("\nbelow this is an unorganized list of all the numbers of lines in each dragon, from 1 to 2 to 3")
    print(possible_max_y_list)

    #this creates the order list through an analysis of the possible_max_y_list. The goal is to arrange the dragons like a winners podium, with the y-values determining the placement
    order_list = []
    while possible_max_y_list:
        if len(possible_max_y_list) == 1:
            order_list.append(max(possible_max_y_list))
            possible_max_y_list.clear()
        
        else:
            order_list.insert(0, max(possible_max_y_list))
            possible_max_y_list.remove(max(possible_max_y_list))
    print("below this is an ordered list of all the numbers of lines in each dragon, arranged like a winners podium")
    print(order_list)
    while order_list:
        if order_list[0] == dragon_1_metadata[2]:
            print("\nprinting dragon 1!")
            order_list.pop(0)
        elif order_list[0] == dragon_2_metadata[2]:
            print("\nprinting dragon 2!")
            order_list.pop(0)
        elif order_list[0] == dragon_3_metadata[2]:
            print("\nprinting dragon 3!")

            dragon_1_line_list = dragon_1.splitlines()
            dragon_2_line_list = dragon_2.splitlines()
            dragon_3_line_list = dragon_3.splitlines()

            print("starting sequence")
            total_line = ""
            #changed this from dragon_1_metadata[2] to dragon_2_metadata[2], since it is the longest of the dragons
            for i in range(0, max_y):
                total_line = ""
                #the rest of this is designed to create a total_line that contains pieces of each dragon in order of middle size, largest, and then smallest, like a winners podium.
                #if a dragon is not long enough to give any more lines to total_lines, then the else block of each region adds blank text in its place. This is currently hard-coded,
                #but a dynamic solution that actually determines the orders of the dragons is in the works. As of now, order list is vestigial. Printing dragon 3!!! was printed because
                #the initial idea was to do it, then dragon_2, then dragon_1, but this fails to recognize how a line from each dragon is needed for total_line. Because of line_lists
                #for each dragon the 0th index of each dragon_metadata is not used, sadly.
                if i < len(dragon_1_line_list) - 1:
                    total_line += dragon_1_line_list[i]
                    if len(dragon_1_line_list[i]) < dragon_1_metadata[1]:
                        for remainder in range(0, dragon_1_metadata[1] - len(dragon_1_line_list[i])):
                            total_line += " "
                else:
                    for remainder in range(0, dragon_1_metadata[1]):
                        total_line += " "
                if i < len(dragon_2_line_list) - 1:
                    total_line += dragon_2_line_list[i]
                    if len(dragon_2_line_list[i]) < dragon_2_metadata[1]:
                        for remainder in range(0, dragon_2_metadata[1] - len(dragon_2_line_list[i])):
                            total_line += " "
                else:
                    for remainder in range(0, dragon_2_metadata[1]):
                        total_line += " "

                if i < len(dragon_3_line_list) - 1:
                    total_line += dragon_3_line_list[i]
                    if len(dragon_3_line_list[i]) < dragon_3_metadata[1]:
                        for remainder in range(0, dragon_3_metadata[1] - len(dragon_3_line_list[i])):
                            total_line += " "
                else:
                    for remainder in range(0, dragon_3_metadata[1]):
                        total_line += " "
                print(total_line)

            print("ending sequence")
                
            #the remaining questions... do we need dragon_metadata[0] anymore, and can we make the dragon printing order dynamic?
            
            break



dragon_1 = """
                                             __----~~~~~~~~~~~------___
                                  .  .   ~~//====......          __--~ ~~
                  -.            \_|//     |||\  ~~~~~~::::... /~
               ___-==_       _-~o~  \/    |||  \            _/~~-
       __---~~~.==~||\=_    -_--~/_-~|-   |\   \        _/~
   _-~~     .=~    |  \-_    '-~7  /-   /  ||    \      /
 .~       .~       |   \ -_    /  /-   /   ||      \   /
/  ____  /         |     \ ~-_/  /|- _/   .||       \ /
|~~    ~~|--~~~~--_ \     ~==-/   | \~--===~~        .\\
         '         ~-|      /|    |-~\~~       __--~~
                     |-~~-_/ |    |   ~\_   _-~            /\\
                          /  \     \__   \/~                \__
                      _--~ _/ | .-~~____--~-/                  ~~==.
                     ((->/~   '.|||' -_|    ~~-/ ,              . _||
                                -_     ~\      ~~---l__i__i__i--~~_/
                                _-~-__   ~)  \--______________--~~
                              //.-~~~-~_--~- |-------~~~~~~~~
                                     //.-~~~--\\
"""
#uhh do we need to do \\ every time???
dragon_2 = """
          /                            )
          (                             |\\
         /|                              \\
        //                                \\
       ///                                 \|
      /( \                                  )\\
      \  \_                               //)
       \  :\__                           ///
        \     )                         // \\
         \:  /                         // |/
          \ / \                       //  \\
           /)   \   ___..-'           (|  \_|
          //     /   _.'              \ \  \\
         /|       \ \________          \ | /
        (| _ _  __/          '-.       ) /.'
         \ .  '-.__            \_    / / \\
          \_'.     > --._ '.     \  / / /
           \ \      \     \  \     .' /.'
            \ \  '._ /     \ )    / .' |
             \ \_     \_   |    .'_/ __/
              \  \      \_ |   / /  _/ \_
               \  \       / _.' /  /     \\
               \   |     /.'   / .'       '-,_
                \   \  .'   _.'_/             \\
   /\    /\      ) ___(    /_.'           \    |
  | _\__// \    (.'      _/               |    |
  \/_  __  /--'`    ,                   __/    /
  (_ ) /b)  \  '.   :            \___.-'_/ \__/
  /:/:  ,     ) :        (      /_.'__/-'|_ _ /
 /:/: __/\ >  __,_.----.__\    /        (/(/(/
(_(,_/V .'/--'    _/  __/ |   /
 VvvV  //`    _.-' _.'     \   \\
   n_n//     (((/->/        |   /
   '--'         ~='          \  |
                              | |_,,,
                              \  \  /
                               '.__)
"""

dragon_3 = """ 
          _.-'.-'-.__
       .-'.       '-.'-._ __.--._
-..'\,-,/..-  _         .'   \   '----._
 ). /_ _\' ( ' '.         '-  '/'-----._'-.__
 '..'     '-r   _      .-.       '-._ \\
 '.\. Y .).'       ( .'  .      .\          '\'.
 .-')'|'/'-.        \)    )      '',_      _.c_.\\
   .<, ,>.          |   _/\        . ',   :   : \\
  .' \_/ '.        /  .'   |          '.     .'  \)
                  / .-'    '-.        : \   _;   ||
                 / /    _     \_      '.'\ ' /   ||
                /.'   .'        \_      .|   \   \|
               / /   /      __.---'      '._  ;  ||
              /.'  _:-.____< ,_           '.\ \  ||
             // .-'     '-.__  '-'-\_      '.\/_ \|
            ( };====.===-==='        '.    .  \: \\
             \ '._        /          :   ,'   )\_ \\
              \   '------/            \ .    /   )/
               \|        _|             )Y    |   /
                \      \             .','   /  ,/
                 \    _/            /     _/
                  \   \           .'    .'
                   '| '1          /    .'
                     '. \        |:    /
                       \ |       /', .'
                        \(      ( ;z'
                         \:      \ '(_
                          \_,     '._ '-.___
                                      '-' -.\\
"""

dragon_printer(dragon_1, dragon_2, dragon_3)