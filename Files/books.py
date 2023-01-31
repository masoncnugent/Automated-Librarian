#All the data for the books as well as a book_types list which stores the name of every book genre in a list.
book_data = [["philosophical", "Beyond Good and Evil", "Fredrich Nietzsche", "1886", "9", "6"],
             ["philosophical", "The Art of War", "Sun Tzu", "5th Century B.C.", "7", "8"],
             ["philosophical", "Republic", "Plato", "375 B.C.", "6", "4"],
             ["philosophical", "Meditations on First Philosophy", "Rene Descartes", "1641", "5", "4"],
             ["philosophical", "Critique of Pure Reason", "Immanuel Kant", "1781", "7", "6"],
             ["poetry", "Where the Sidewalk Ends", "Shel Silverstein", "1974", "5", "4"],
             ["poetry", "Leaves of Grass", "Walt Whitman", "1855", "7", "5"],
             ["poetry", "100 Selected Poems", "E. E. Cummings", "1954", "4", "4"],
             ["poetry", "The Complete Poems", "Emily Dickinson", "1955", "6", "7"],
             ["poetry", "Divine Comedy", "Dante Alighieri", "1971", "6", "7"],
             ["poetry", "Shakespeare's Sonnets and Poems", "William Shakespeare", "1609", "8", "3"],
             ["comic strip", "It's a Magical World", "Bill Watterson", "1996", "10", "10"],
             ["comic strip", "Garfield at Large: His First Book", "Jim Davis", "1980", "2", "1"],
             ["comic strip", "The Complete Peanuts", "Charles M. Shulz", "1952", "4", "7"],
             ["comic strip", "Watchmen", "Alan Moore", "1986", "5", "7"],
             ["comic strip", "Dilbert", "Scott Adams", "1989", "4", "5"],
             ["comedy", "Based on a True Story: A Memoir", "Norm Macdonald", "2016", "6", "7"],
             ["comedy", "The Importance of Being Earnest", "Oscar Wilde", "1895", "5", "5"],
             ["cooking", "Mastering the Art of French Cooking", "Julia Child", "1961", "8", "7"],
             ["cooking", "Joy of Cooking", "1931", "Imma S. Rombauer", "9", "9"],
             ["cooking", "The Taste of Country Cooking", "Edna Lewis", "1976", "6", "7"],
             ["adventure", "Moby-Dick", "Herman Melville", "1851", "4", "7"],
             ["adventure", "The Call of the Wild", "Jack London", "1903", "4", "5"],
             ["adventure", "Hatchet", "Gary Paulsen", "1986", "4", "5"],
             ["art", "The Art Book", "Phaidon Press", "1994", "5", "6"],
             ["art", "The Usborne Book of Famous Artists", "Ruth Brocklehurst", "2012", "4", "5"],
             ["english curriculum", "Frankenstein", "Mary Shelley", "1818", "7", "8"],
             ["english curriculum", "Catcher on the Rye", "J. D. Salinger", "1945", "5", "2"],
             ["english curriculum", "Lord of the Flies", "William Golding", "1954", "7", "4"],
             ["english curriculum", "The Great Gatsby", "F. Scott Fitzgerald", "1925", "6", "5"],
             ["english curriculum", "1984", "George Orwell", "1949", "8", "9"],
             ["epic", "The Illiad and the Odyssey", "Homer","7th Century B.C.", "7", "8"],
             ["epic", "The Aeneid", "Virgil", "19 B.C.", "6", "5"],
             ["epic", "Paradise Lost", "John Milton", "1667", "5", "4"]]

potential_types = [type[0] for type in book_data]
book_types = []
for type in potential_types:
    if type not in book_types:
        book_types.append(type)