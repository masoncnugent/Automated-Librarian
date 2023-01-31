#Creates the data on each 'creature' (they used to be all dragons until I had the bright idea of adding Pokémon) so creature_printer knows how to add whitespace (Braille Unicode Blank) in between each creature when printed side-by-side.
def creature_metadata_maker(creature):
    creature_data = creature.splitlines()
    temp_line_length_list = []
    for line in creature_data:
        temp_line_length_list.append(len(line))
    #The line below this gets rid of the newline that exists at the start of each creature because of where the """ marks start.
    creature_data.pop(0)
    creature_x = max(temp_line_length_list)
    creature_y = len(temp_line_length_list)
    #The +5 is for spacing between the creatures.
    return creature_data, creature_x + 5, creature_y

#Prints the creatures to the screen. Hard-coded to work with 3 creatures, but it dynamically sorts them by y-axis size to be displayed in order of 2, 1, 3; a winner's podium.
def creature_printer(creature_1, creature_2, creature_3):
    creature_1 = creature_1
    creature_2 = creature_2
    creature_3 = creature_3

    creature_1_metadata = creature_metadata_maker(creature_1)
    creature_2_metadata = creature_metadata_maker(creature_2)
    creature_3_metadata = creature_metadata_maker(creature_3)

    #Getting the creatures printing properly when already ordered is easy, so the pipeline flow is ordering, (which follows this comment,) assignment, and then printing.
    axis_metadata_list = []
    axis_metadata_list.append([creature_1_metadata[1]])
    axis_metadata_list[0].append(creature_1_metadata[2])
    axis_metadata_list.append([creature_2_metadata[1]])
    axis_metadata_list[1].append(creature_2_metadata[2])
    axis_metadata_list.append([creature_3_metadata[1]])
    axis_metadata_list[2].append(creature_3_metadata[2])

    possible_max_y_list = []
    for possible_max_y in axis_metadata_list:
        possible_max_y_list.append(possible_max_y[1])

    #This is used later when determining for how long the creature printing process should be.
    max_y = max(possible_max_y_list)

    #This creates the y_axis_order list through an analysis of the possible_max_y_list. The goal is to arrange the creatures like a winners podium, with higher y-axis maximums ranking higher than lower.
    y_axis_order_list = []
    while possible_max_y_list:
        if len(possible_max_y_list) == 1:
            y_axis_order_list.append(possible_max_y_list[0])
            possible_max_y_list.clear()
        
        else:
            y_axis_order_list.insert(0, max(possible_max_y_list))
            possible_max_y_list.remove(max(possible_max_y_list))

    #both_axes_order_list was created to prevent competition between creatures with the same y-axis maximum, with the first creature added to possible_max_y_list inevitably being printed twice, but I ended up using creature_x_chosen.
    #In that way, having both axes saved is redundant, but it took a lot of effort to save them both, and the problem solving strategy needed to save both axes ordered in the winners podium style is worth keeping it as a testament.
    both_axes_order_list = []
    for item in y_axis_order_list.copy():
        for axis_metadata in axis_metadata_list.copy():
            if axis_metadata[1] == item:
                both_axes_order_list.append(axis_metadata)
                y_axis_order_list.pop(0)
                axis_metadata_list.remove(axis_metadata)
                break

    #Ordering the data of the creatures is already done, but now that data needs to be used to assign all the creature data to the proper creature.
    id = 1
    creature_1_chosen = False
    creature_2_chosen = False
    creature_3_chosen = False

    for entry in both_axes_order_list:
        if id == 1:
            if creature_1_metadata[1] == entry[0] and creature_1_metadata[2] == entry[1] and creature_1_chosen == False:
                first_creature_line_list = creature_1_metadata[0]
                first_creature_metadata = creature_1_metadata
                creature_1_chosen = True
            elif creature_2_metadata[1] == entry[0] and creature_2_metadata[2] == entry[1] and creature_2_chosen == False:
                first_creature_line_list = creature_2_metadata[0]
                first_creature_metadata = creature_2_metadata
                creature_2_chosen = True
            elif creature_3_metadata[1] == entry[0] and creature_3_metadata[2] == entry[1] and creature_3_chosen == False:
                first_creature_line_list = creature_3_metadata[0]
                first_creature_metadata = creature_3_metadata
                creature_3_chosen = True
            id += 1
        elif id == 2:

            if creature_1_metadata[1] == entry[0] and creature_1_metadata[2] == entry[1] and creature_1_chosen == False:
                second_creature_line_list = creature_1_metadata[0]
                second_creature_metadata = creature_1_metadata
                creature_1_chosen = True
            elif creature_2_metadata[1] == entry[0] and creature_2_metadata[2] == entry[1] and creature_2_chosen == False:
                second_creature_line_list = creature_2_metadata[0]
                second_creature_metadata = creature_2_metadata
                creature_2_chosen = True
            elif creature_3_metadata[1] == entry[0] and creature_3_metadata[2] == entry[1] and creature_3_chosen == False:
                second_creature_line_list = creature_3_metadata[0]
                second_creature_metadata = creature_3_metadata
                creature_3_chosen = True
            id += 1
        elif id == 3:
            if creature_1_metadata[1] == entry[0] and creature_1_metadata[2] == entry[1] and creature_1_chosen == False:
                third_creature_line_list = creature_1_metadata[0]
                third_creature_metadata = creature_1_metadata
                creature_1_chosen = True
            elif creature_2_metadata[1] == entry[0] and creature_2_metadata[2] == entry[1] and creature_2_chosen == False:
                third_creature_line_list = creature_2_metadata[0]
                third_creature_metadata = creature_2_metadata
                creature_2_chosen = True
            elif creature_3_metadata[1] == entry[0] and creature_3_metadata[2] == entry[1] and creature_3_chosen == False:
                third_creature_line_list = creature_3_metadata[0]
                third_creature_metadata = creature_3_metadata
                creature_3_chosen = True

    total_line = ""

    #This is the printing portion of the creature pipeline.
    for i in range(0, max_y):
        total_line = ""

        #The remainder added used to be whitespace, but since all the creatures use Braille Unicode Blank, it was changed to that.
        offset = ((max_y - first_creature_metadata[2]) // 2)
        if offset <= i < len(first_creature_line_list) + offset:
            total_line += first_creature_line_list[i - offset]
            if len(first_creature_line_list[i - offset]) < first_creature_metadata[1]:
                for remainder in range(0, first_creature_metadata[1] - len(first_creature_line_list[i - offset])):
                    total_line += "⠀"
        else:
            for remainder in range(0, first_creature_metadata[1]):
                total_line += "⠀"
        
        offset = ((max_y - second_creature_metadata[2]) // 2)
        if offset <= i < len(second_creature_line_list) + offset:
            total_line += second_creature_line_list[i - offset]
            if len(second_creature_line_list[i - offset]) < second_creature_metadata[1]:
                for remainder in range(0, second_creature_metadata[1] - len(second_creature_line_list[i - offset])):
                    total_line += "⠀"
        else:
            for remainder in range(0, second_creature_metadata[1]):
                total_line += "⠀"

        offset = ((max_y - third_creature_metadata[2]) // 2)
        if offset <= i < len(third_creature_line_list) + offset:
            total_line += third_creature_line_list[i - offset]
            if len(third_creature_line_list[i - offset]) < third_creature_metadata[1]:
                for remainder in range(0, third_creature_metadata[1] - len(third_creature_line_list[i - offset])):
                    total_line += "⠀"
        else:
            for remainder in range(0, third_creature_metadata[1]):
                total_line += "⠀"
        print(total_line)

    #This prints the title of the program surrounded by bars. It's automated to center itself between the 3 creatures chosen to be put into creature_printer(). The -5 is for the whitespace added to metadata to space each creature
    title_total_length = creature_1_metadata[1] + creature_2_metadata[1] + creature_3_metadata[1] - 5
    title_segment = "Welcome To The Automated Librarian!!"
    title_segment_length = len(title_segment)
    #This centers the title around the location of the middle creature.
    welcome_offset = (first_creature_metadata[1] + ((second_creature_metadata[1] - 5) // 2)) - (title_segment_length // 2)

    bars = ""
    #for i in range(0, gap_length):
    for i in range(0, welcome_offset):
        bars += "⠀"
        gap = bars

    for i in range(title_segment_length):
        bars += "="
    bars += gap

    print("\n\n" + bars)
    print(gap + title_segment)
    print(bars)

    #This is NOT what this function is about, this is just so the 'x's around the book categories go for the appropriate length
    return title_total_length