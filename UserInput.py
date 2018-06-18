class UserInput():

    @classmethod
    def string_input(cls):
        '''
        ask for user input for a string then return the string
        '''
        string = None
        is_string = False
        while not is_string:
            try:
                string = str(input('Please enter a string: '))
                is_string = True
            except:
                print('Invalid input, please enter a string!')
        print('==========================================')
        return string

    @classmethod
    def letter_input(cls):
        '''
        ask for user input for a string then return the string
        '''
        letter = None
        is_letter = False
        while not is_letter:
            try:
                letter = str(input('Please enter a letter: '))
                if len(letter) == 1:
                    is_letter = True
                else:
                    print('Invalid input, please enter a letter!')
            except:
                print('Invalid input, please enter a letter!')
        print('==========================================')
        return letter

    @classmethod
    def int_input(cls, int_min = -10000, int_max=10000):
        '''
        ask for user input for a integer in a certain range
        then return the integer
        '''
        int_num = None
        is_int = False
        while not is_int:
            try:
                int_num = int(input('Please enter a integer: '))
                if int_num in range(int_min, int_max + 1):
                    is_int = True
                else:
                    print('Invalid input, please enter a integer from {} to {}!'.format(int_min, int_max))
            except:
                print('Invalid input, please enter a integer from {} to {}!'.format(int_min, int_max))
        print('==========================================')
        return int_num

    @classmethod
    def num_input(cls):
        '''
        ask for user input for a number then return the number
        '''
        float_num = None
        is_num = False
        while not is_num:
            try:
                float_num = float(input('Please enter a number: '))
                is_num = True
            except:
                print('Invalid input, please enter a number!')
        print('==========================================')
        return float_num
