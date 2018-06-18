class WordLib():

    wordlib_menu = Menu('Word Library Menu', ['Show all words', 'Show by category', 'Add new word', 'Delete word','Exit'])
    catergory_menu = Menu('Category', ['Computer Science', 'Fruit', 'Places', 'Names'])
    computer_science = ['programming', 'programming language', 'Python', 'Coding Temple',
                        'Jupyter Notebook', 'algorithm', 'data structure', 'operating sytem', 'machine learning', 'time complexity']
    fruit = ['apple', 'banana', 'peach', 'orange', 'watermelon', 'kiwi', 'mango', 'pineapple']
    places = ['Downtown Crossing', 'Back Bay','Cambridge', 'Chinatown', 'Somerville', 'Harvard Square',
             'Porter Square']
    names = ['Dan', 'Jeff', 'Rob', 'Ethan', 'Jamie', 'Matt', 'Clay']
    wordlib = computer_science + fruit + places + names

    @classmethod
    def random_word(cls):
        a_word = random.choice(cls.wordlib)
        return a_word

    @classmethod
    def show_word_info(cls, a_word):
        if a_word in cls.computer_science:
            print('This word is related to Computer Science.')
        elif a_word in cls.fruit:
            print('This word is the name of a fruit.')
        elif a_word in cls.places:
            print('This word is the name of a place in Boston.')
        elif a_word in cls.names:
            print('This word is the name of one of our classmates.')
        print('==========================================')
        #print(' ')

    @classmethod
    def show_wordlib_menu(cls):
        cls.wordlib_menu.show_menu()

    @classmethod
    def show_by_category(cls):
        print('Pleae select a category.')
        cls.catergory_menu.show_menu()
        option = UserInput.int_input(0, cls.catergory_menu.menu_length() - 1)
        if option == 0:
            print('Computer Science')
            print('==========================================')
            print(cls.computer_science)
        elif option == 1:
            print('Fruit')
            print('==========================================')
            print(cls.fruit)
        elif option == 2:
            print('Places')
            print('==========================================')
            print(cls.places)
        elif option == 3:
            print('Names')
            print('==========================================')
            print(cls.names)

    @classmethod
    def show_all(cls):
        print('All words in library')
        print('==========================================')
        print(cls.wordlib)

    @classmethod
    def update_wordlib(cls):
        cls.wordlib = cls.computer_science + cls.fruit + cls.places + cls.names

    @classmethod
    def check_exist(cls, word, word_list):
        for i, v in enumerate(word_list):
            if word.lower() == word_list[i].lower():
                print('==========================================')
                print('{} is alreay in the library!'.format(word))
                #print('Please enter another word!')
                print('==========================================')
                return True
        print('==========================================')
        print('{} is not in the library!'.format(word))
        #print('Please enter another word!')
        print('==========================================')
        return False

    @classmethod
    def add_to_wordlib(cls):
        print('You can now add word to the word library.')
        print('==========================================')
        print('Enter the word you want to add.')
        flag = True
        while flag:
            add_word = UserInput.string_input()
            is_exist = cls.check_exist(add_word, WordLib.wordlib)
            if is_exist == False:
                flag = False
            else:
                print('Please enter another word!')
        cls.catergory_menu.show_menu()
        print('Choose a category which the new word will be added.')
        category_num = UserInput.int_input(0, cls.catergory_menu.menu_length() - 1)
        if category_num == 0:
            cls.computer_science.append(add_word)
            print('{} has been successfully added!'.format(add_word))
        elif category_num == 1:
            cls.fruit.append(add_word)
            print('{} has been successfully added!'.format(add_word))
        elif category_num == 2:
            cls.places.append(add_word)
            print('{} has been successfully added!'.format(add_word))
        elif category_num == 3:
            cls.names.append(add_word)
            print('{} has been successfully added!'.format(add_word))
        cls.update_wordlib()

    @classmethod
    def delete_from_wrodlib(cls):
        print('You can now delete word from the word library.')
        print('==========================================')
        cls.catergory_menu.show_menu()
        print('Choose a category from which you want to delete.')
        category_num = UserInput.int_input(0, cls.catergory_menu.menu_length() - 1)
        if category_num == 0:
            cs_menu = Menu('Computer Science', cls.computer_science)
            cs_menu.show_menu()
            print('Choose the word you want to delete.')
            word_num = UserInput.int_input(0, cs_menu.menu_length() - 1)
            word_deleted = cls.computer_science[word_num]
            del cls.computer_science[word_num]
            print('{} has been successfully deleted!'.format(word_deleted))
        elif category_num == 1:
            fruit_menu = Menu('Fruit', cls.fruit)
            fruit_menu.show_menu()
            print('Choose the word you want to delete.')
            word_num = UserInput.int_input(0, fruit_menu.menu_length() - 1)
            word_deleted = WordLib.fruit[word_num]
            del cls.fruit[word_num]
            print('{} has been successfully deleted!'.format(word_deleted))
        elif category_num == 2:
            places_menu = Menu('Places', cls.places)
            places_menu.show_menu()
            print('Choose the word you want to delete.')
            word_num = UserInput.int_input(0, places_menu.menu_length() - 1)
            word_deleted = WordLib.places[word_num]
            del cls.places[word_num]
            print('{} has been successfully deleted!'.format(word_deleted))
        elif category_num == 3:
            names_menu = Menu('Names', cls.names)
            names_menu.show_menu()
            print('Choose the word you want to delete.')
            word_num = UserInput.int_input(0, names_menu.menu_length() - 1)
            word_deleted = WordLib.names[word_num]
            del cls.names[word_num]
            print('{} has been successfully deleted!'.format(word_deleted))
        cls.update_wordlib()

    @classmethod
    def wordlib_main(cls):
        exit = False
        while not exit:
            #clear_output()
            cls.show_wordlib_menu()
            print('Enter your option.')
            option = UserInput.int_input(0, cls.wordlib_menu.menu_length() - 1)

            if option == 0:
                clear_output()
                cls.show_all()
            elif option == 1:
                clear_output()
                cls.show_by_category()
            elif option == 2:
                clear_output()
                cls.add_to_wordlib()
            elif option == 3:
                clear_output()
                cls.delete_from_wrodlib()
            elif option == 4:
                clear_output()
                exit = True
                print('==========================================')
                print('Exiting Word Library....Bye!')
                print('==========================================')
