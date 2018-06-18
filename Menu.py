class Menu():

    def __init__(self, name = 'Default Menu', menu = ['Option 0', 'Option 1', 'Option 2']):
        self.menu = menu
        self.name = name
        
    def show_menu(self):
        print('==========================================')
        print(self.name)
        print('==========================================')
        for i, item in enumerate(self.menu):
            print('{} -----> {}'.format(i, item))
        print('==========================================')

    def menu_length(self):
        return len(self.menu)

    def modify_menu(self):
        print('You can modify the menu now.')
        print('==========================================')
        self.show_menu()

        print('Please select a option you want to modify: ')
        option_number = UserInput.int_input(0, self.menu_length() - 1)
        print('{} -----> {} selected!'.format(option_number, self.menu[option_number]))
        print('Please modify option {}: '.format(option_number))
        new_name = UserInput.string_input()
        self.menu[option_number] = new_name
        print('Option {} is modified to {} cuccessfully!'.format(option_number, new_name))
        print('==========================================')
