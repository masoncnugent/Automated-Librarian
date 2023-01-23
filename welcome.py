def dragon_metadata_maker(dragon):
    dragon_data = dragon.splitlines()
    temp_line_length_list = []
    for line in dragon_data:
        temp_line_length_list.append(len(line))
    #the line below this gets rid of the newline that exists at the start of each dragon because of where the """ marks start
    dragon_data.pop(0)
    print("does dragon_data have issues here?")
    print(dragon_data)
    dragon_x = max(temp_line_length_list)
    dragon_y = len(temp_line_length_list)
    return dragon_data, dragon_x, dragon_y

#prints the dragons to the screen. Hard-coded to work with 3 dragons, but it dynamically sorts them by size to be displayed in order of 2, 1, 3, a winner's podium
def dragon_printer(dragon_1, dragon_2, dragon_3):
    dragon_1 = dragon_1
    dragon_2 = dragon_2
    dragon_3 = dragon_3
    dragon_1_metadata = dragon_metadata_maker(dragon_1)
    dragon_2_metadata = dragon_metadata_maker(dragon_2)
    dragon_3_metadata = dragon_metadata_maker(dragon_3)

    possible_max_y_list = []
    possible_max_y_list.append(dragon_1_metadata[2])
    possible_max_y_list.append(dragon_2_metadata[2])
    possible_max_y_list.append(dragon_3_metadata[2])

    max_y = max(possible_max_y_list)

    #this creates the order list through an analysis of the possible_max_y_list. The goal is to arrange the dragons like a winners podium, with the y-values determining the placement
    order_list = []
    while possible_max_y_list:
        if len(possible_max_y_list) == 1:
            order_list.append(max(possible_max_y_list))
            possible_max_y_list.clear()
        
        else:
            order_list.insert(0, max(possible_max_y_list))
            possible_max_y_list.remove(max(possible_max_y_list))

    id = 1
    for entry in order_list:
        if id == 1:
            if dragon_1_metadata[2] == entry:
                first_dragon_line_list = dragon_1_metadata[0]
                first_dragon_metadata = dragon_1_metadata
            elif dragon_2_metadata[2] == entry:
                first_dragon_line_list = dragon_2_metadata[0]
                first_dragon_metadata = dragon_2_metadata
            elif dragon_3_metadata[2] == entry:
                first_dragon_line_list = dragon_3_metadata[0]
                first_dragon_metadata = dragon_3_metadata
            id += 1
        elif id == 2:
            if dragon_1_metadata[2] == entry:
                second_dragon_line_list = dragon_1_metadata[0]
                second_dragon_metadata = dragon_1_metadata
            elif dragon_2_metadata[2] == entry:
                second_dragon_line_list = dragon_2_metadata[0]
                second_dragon_metadata = dragon_2_metadata
            elif dragon_3_metadata[2] == entry:
                second_dragon_line_list = dragon_3_metadata[0]
                second_dragon_metadata = dragon_3_metadata
            id += 1
        elif id == 3:
            if dragon_1_metadata[2] == entry:
                third_dragon_line_list = dragon_1_metadata[0]
                third_dragon_metadata = dragon_1_metadata
            elif dragon_2_metadata[2] == entry:              
                third_dragon_line_list = dragon_2_metadata[0]
                third_dragon_metadata = dragon_2_metadata
            elif dragon_3_metadata[2] == entry:
                third_dragon_line_list = dragon_3_metadata[0]
                third_dragon_metadata = dragon_3_metadata

    total_line = ""

    for i in range(0, max_y):
        total_line = ""

        offset = ((max_y - first_dragon_metadata[2]) // 2)
        if offset < i < len(first_dragon_line_list) + offset - 1:
            total_line += first_dragon_line_list[i - offset]
            if len(first_dragon_line_list[i - offset]) < first_dragon_metadata[1]:
                for remainder in range(0, first_dragon_metadata[1] - len(first_dragon_line_list[i - offset])):
                    total_line += " "
        else:
            for remainder in range(0, first_dragon_metadata[1]):
                total_line += " "
        
        offset = ((max_y - second_dragon_metadata[2]) // 2)
        if offset < i < len(second_dragon_line_list) + offset - 1:
            total_line += second_dragon_line_list[i - offset]
            if len(second_dragon_line_list[i - offset]) < second_dragon_metadata[1]:
                for remainder in range(0, second_dragon_metadata[1] - len(second_dragon_line_list[i - offset])):
                    total_line += " "
        else:
            for remainder in range(0, second_dragon_metadata[1]):
                total_line += " "

        offset = ((max_y - third_dragon_metadata[2]) // 2)
        if offset < i < len(third_dragon_line_list) + offset - 1:
            total_line += third_dragon_line_list[i - offset]
            if len(third_dragon_line_list[i - offset]) < third_dragon_metadata[1]:
                for remainder in range(0, third_dragon_metadata[1] - len(third_dragon_line_list[i - offset])):
                    total_line += " "
        else:
            for remainder in range(0, third_dragon_metadata[1]):
                total_line += " "
        print(total_line)

    print("\n                                                                               =====================================")
    print("                                                                               Welcome To The Automated Librarian!!!")
    print("                                                                               =====================================")


dragon_goofy = """
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

dragon_scary = """
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

dragon_aloofy = """ 
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